#!/usr/bin/env python3
"""Fetch Keyword Planner figures for one client's market.

Reads ~/.config/website-builder/google-ads.json, or the path in
WEBSITE_BUILDER_GOOGLE_ADS_CONFIG. That file holds customer_id and
service_account_key_file. The key never belongs in a website or in git.

Python 3.10+ standard library. Signing uses the openssl already on the machine.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://googleads.googleapis.com/v26"
TOKEN_URL = "https://oauth2.googleapis.com/token"
SCOPE = "https://www.googleapis.com/auth/adwords"
CACHE_TTL = 24 * 60 * 60


class PlannerError(Exception):
    """A Keyword Planner failure the caller can report without inventing numbers."""


def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def config_path() -> Path:
    override = os.environ.get("WEBSITE_BUILDER_GOOGLE_ADS_CONFIG")
    if override:
        return Path(override)
    return Path.home() / ".config" / "website-builder" / "google-ads.json"


def load_config() -> tuple[str, Path]:
    path = config_path()
    if not path.is_file():
        raise PlannerError(
            f"Missing {path}. It needs customer_id and service_account_key_file, "
            "kept outside the website and outside git."
        )
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise PlannerError(f"{path} is not valid JSON.") from exc
    customer = str(data.get("customer_id", "")).replace("-", "").strip()
    key_file = data.get("service_account_key_file")
    if not customer.isdigit() or not key_file:
        raise PlannerError(f"{path} needs customer_id and service_account_key_file.")
    key_path = Path(key_file)
    if not key_path.is_file():
        raise PlannerError(f"Service account key not found at {key_path}.")
    return customer, key_path


def access_token(key_path: Path) -> str:
    try:
        key = json.loads(key_path.read_text())
        email = key["client_email"]
        private_key = key["private_key"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise PlannerError(f"{key_path} is not a service account key.") from exc
    now = int(time.time())
    header = b64(json.dumps({"alg": "RS256", "typ": "JWT"}, separators=(",", ":")).encode())
    claims = {
        "iss": email,
        "scope": SCOPE,
        "aud": TOKEN_URL,
        "iat": now,
        "exp": now + 3600,
    }
    payload = b64(json.dumps(claims, separators=(",", ":")).encode())
    signing = f"{header}.{payload}".encode()
    pem = tempfile.NamedTemporaryFile("w", delete=False)
    try:
        pem.write(private_key)
        pem.close()
        os.chmod(pem.name, 0o600)
        signature = subprocess.check_output(
            ["openssl", "dgst", "-sha256", "-sign", pem.name],
            input=signing,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise PlannerError("Could not sign the Ads request with openssl.") from exc
    finally:
        os.unlink(pem.name)
    body = urllib.parse.urlencode(
        {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": f"{signing.decode()}.{b64(signature)}",
        }
    ).encode()
    request = urllib.request.Request(TOKEN_URL, data=body, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            token = json.load(response)["access_token"]
    except (urllib.error.URLError, KeyError, json.JSONDecodeError) as exc:
        raise PlannerError("Google refused the service account token.") from exc
    return token


def ads_request(token: str, method: str, url: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(url, data=data, method=method)
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode()
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"error": {"message": raw[:400]}}
        message = payload.get("error", {}).get("message", "request failed")
        codes: list[str] = []
        for detail in payload.get("error", {}).get("details", []):
            for error in detail.get("errors", []):
                code = error.get("errorCode") or {}
                if code:
                    codes.append(next(iter(code.values())))
        suffix = f" ({', '.join(codes)})" if codes else ""
        raise PlannerError(f"Google Ads API returned {exc.code}: {message}{suffix}") from exc
    except urllib.error.URLError as exc:
        raise PlannerError("Could not reach the Google Ads API.") from exc


def search(token: str, customer: str, query: str) -> list[dict]:
    payload = ads_request(
        token,
        "POST",
        f"{API}/customers/{customer}/googleAds:search",
        {"query": query},
    )
    return payload.get("results") or []


def place_constant(token: str, customer: str, country: str, place: str, place_id: str | None = None) -> tuple[str, str]:
    if not place or len(place) > 81 or not place[0].isalpha() or not all(c.isalpha() or c in " .'-" for c in place):
        raise PlannerError("A place name can use letters, spaces, apostrophes, and hyphens.")
    escaped = place.replace("'", "\\'")
    rows = search(
        token,
        customer,
        "SELECT geo_target_constant.resource_name, geo_target_constant.name, "
        "geo_target_constant.canonical_name, geo_target_constant.target_type "
        "FROM geo_target_constant "
        f"WHERE geo_target_constant.country_code = '{country}' "
        f"AND geo_target_constant.name = '{escaped}' "
        "AND geo_target_constant.status = 'ENABLED'",
    )
    choices = [row.get("geoTargetConstant") or {} for row in rows]
    if place_id:
        choices = [item for item in choices if item.get("resourceName") == f"geoTargetConstants/{place_id}"]
    if len(choices) == 1:
        picked = choices[0]
    elif not choices:
        raise PlannerError(
            f"No Keyword Planner place named {place} in {country}. "
            "Ask for a clearer place. Do not substitute the whole country."
        )
    else:
        names = ", ".join(f"{item.get('canonicalName') or item.get('name', '')} [{item.get('targetType')}, ID {item.get('resourceName', '').split('/')[-1]}]" for item in choices[:8])
        raise PlannerError(f"Several places match {place}: {names}. Ask which one, then pass its --place-id.")
    label = picked.get("canonicalName") or picked.get("name") or place
    return picked["resourceName"], label


def country_constant(token: str, customer: str, country: str) -> str:
    rows = search(
        token,
        customer,
        "SELECT geo_target_constant.resource_name "
        "FROM geo_target_constant "
        f"WHERE geo_target_constant.country_code = '{country}' "
        "AND geo_target_constant.target_type = 'Country'",
    )
    if not rows:
        raise PlannerError(f"No Keyword Planner country for {country}.")
    return rows[0]["geoTargetConstant"]["resourceName"]


def language_constant(token: str, customer: str, language: str) -> str:
    rows = search(
        token,
        customer,
        "SELECT language_constant.resource_name "
        "FROM language_constant "
        f"WHERE language_constant.code = '{language}'",
    )
    if not rows:
        raise PlannerError(f"No Keyword Planner language for {language}.")
    return rows[0]["languageConstant"]["resourceName"]


def currency_code(token: str, customer: str) -> str | None:
    rows = search(token, customer, "SELECT customer.currency_code FROM customer LIMIT 1")
    if not rows:
        return None
    return rows[0].get("customer", {}).get("currencyCode")


def money(micros: str | None) -> float | None:
    if micros is None:
        return None
    return round(int(micros) / 1_000_000, 2)


def metric_row(item: dict) -> dict:
    metrics = item.get("keywordIdeaMetrics") or item.get("keywordMetrics") or {}
    history = []
    for point in metrics.get("monthlySearchVolumes") or []:
        history.append(
            {
                "year": int(point["year"]),
                "month": point["month"],
                "searches": int(point["monthlySearches"]),
            }
        )
    searches = metrics.get("avgMonthlySearches")
    return {
        "keyword": item.get("text"),
        "avg_monthly_searches": int(searches) if searches is not None else None,
        "ads_competition": metrics.get("competition"),
        "low_top_of_page_bid": money(metrics.get("lowTopOfPageBidMicros")),
        "high_top_of_page_bid": money(metrics.get("highTopOfPageBidMicros")),
        "monthly_searches": history,
        "close_variants": item.get("closeVariants") or [],
    }


def fetch_ideas(
    token: str,
    customer: str,
    *,
    language: str,
    geo: str,
    seeds: list[str],
    urls: list[str],
    limit: int,
) -> list[dict]:
    body: dict = {
        "language": language,
        "geoTargetConstants": [geo],
        "keywordPlanNetwork": "GOOGLE_SEARCH",
        "pageSize": limit,
    }
    if seeds and urls:
        body["keywordAndUrlSeed"] = {"keywords": seeds, "url": urls[0]}
    elif urls:
        body["urlSeed"] = {"url": urls[0]}
    else:
        body["keywordSeed"] = {"keywords": seeds}
    payload = ads_request(
        token,
        "POST",
        f"{API}/customers/{customer}:generateKeywordIdeas",
        body,
    )
    return [metric_row(item) for item in payload.get("results") or []]


def fetch_historical(
    token: str,
    customer: str,
    *,
    language: str,
    geo: str,
    keywords: list[str],
) -> list[dict]:
    payload = ads_request(
        token,
        "POST",
        f"{API}/customers/{customer}:generateKeywordHistoricalMetrics",
        {
            "language": language,
            "geoTargetConstants": [geo],
            "keywordPlanNetwork": "GOOGLE_SEARCH",
            "keywords": keywords,
        },
    )
    return [metric_row(item) for item in payload.get("results") or []]


def cache_file(material: dict) -> Path:
    digest = hashlib.sha256(json.dumps(material, sort_keys=True).encode()).hexdigest()
    folder = Path.home() / ".cache" / "website-builder" / "keyword-planner"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{digest}.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Keyword Planner figures for a client market.")
    parser.add_argument("--country", required=True, help="Two-letter country code the owner named. There is no default.")
    parser.add_argument("--language", required=True, help="Language code the owner wants on the site.")
    parser.add_argument("--place", help="City or region the owner named. Omit for a country they said is national.")
    parser.add_argument("--place-id", help="Confirmed ID from ambiguous --place results; requires --place.")
    parser.add_argument("--seed", action="append", default=[], help="Service or business phrase. Repeat for each.")
    parser.add_argument("--url", action="append", default=[], help="Site or competitor URL used as a seed.")
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Existing phrase. Repeat to request historical metrics instead of ideas.",
    )
    parser.add_argument("--limit", type=int, default=20, help="Maximum ideas to return (1-100).")
    parser.add_argument("--refresh", action="store_true", help="Ignore a cached result from the last 24 hours.")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z]{2}", args.country):
        parser.error("--country must be a two-letter code")
    if not re.fullmatch(r"[A-Za-z]{2,3}", args.language):
        parser.error("--language must be a two- or three-letter code")
    if args.place_id and (not args.place or not args.place_id.isdigit()):
        parser.error("--place-id must be numeric and used with --place")
    if len(args.url) > 1:
        parser.error("pass only one --url per request; run separate requests for other sites")
    if args.keyword and (args.seed or args.url):
        parser.error("use --keyword on its own, or --seed/--url for new ideas")
    if not args.keyword and not args.seed and not args.url:
        parser.error("pass at least one --seed, --url, or --keyword")
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be from 1 to 100")
    args.country = args.country.upper()
    args.language = args.language.lower()
    return args


def main() -> int:
    args = parse_args()
    try:
        customer, key_path = load_config()
    except PlannerError as exc:
        print(exc, file=sys.stderr)
        return 1
    material = {
        "customer_id": customer,
        "api": API,
        "place_id": args.place_id,
        "country": args.country,
        "place": args.place,
        "language": args.language,
        "seeds": args.seed,
        "urls": args.url,
        "keywords": args.keyword,
        "limit": args.limit,
    }
    cached = cache_file(material)
    if not args.refresh and cached.is_file():
        age = time.time() - cached.stat().st_mtime
        if age < CACHE_TTL:
            try:
                stored = json.loads(cached.read_text())
            except (OSError, ValueError):
                stored = None
            if isinstance(stored, dict) and isinstance(stored.get("keywords"), list):
                stored["cached"] = True
                json.dump(stored, sys.stdout, indent=2)
                sys.stdout.write("\n")
                return 0
    try:
        token = access_token(key_path)
        place_label = None
        if args.place:
            geo, place_label = place_constant(token, customer, args.country, args.place, args.place_id)
        else:
            geo = country_constant(token, customer, args.country)
        language = language_constant(token, customer, args.language)
        if args.keyword:
            rows = fetch_historical(token, customer, language=language, geo=geo, keywords=args.keyword)
            kind = "historical"
        else:
            rows = fetch_ideas(
                token,
                customer,
                language=language,
                geo=geo,
                seeds=args.seed,
                urls=args.url,
                limit=args.limit,
            )
            kind = "ideas"
        result = {
            "country": args.country,
            "place": place_label,
            "language": args.language,
            "currency_code": currency_code(token, customer),
            "fetched_on": time.strftime("%Y-%m-%d"),
            "result": kind,
            "cached": False,
            "keywords": rows,
        }
    except PlannerError as exc:
        print(exc, file=sys.stderr)
        return 1
    cached.write_text(json.dumps(result, indent=2) + "\n")
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
