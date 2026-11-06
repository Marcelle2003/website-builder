import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("keyword_ideas", Path(__file__).resolve().parents[1] / "skills/website-builder/scripts/keyword_ideas.py")
k = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(k)

class KeywordTests(unittest.TestCase):
    def places(self):
        return [{"geoTargetConstant": {"resourceName": "geoTargetConstants/1", "targetType": "City", "canonicalName": "New York City"}}, {"geoTargetConstant": {"resourceName": "geoTargetConstants/2", "targetType": "State", "canonicalName": "New York State"}}]

    def test_ambiguous_city_and_region_requires_choice(self):
        with patch.object(k, "search", return_value=self.places()):
            with self.assertRaisesRegex(k.PlannerError, "Several places"):
                k.place_constant("token", "123", "US", "New York")
            self.assertEqual(k.place_constant("token", "123", "US", "New York", "2"), ("geoTargetConstants/2", "New York State"))
            with self.assertRaises(k.PlannerError):
                k.place_constant("token", "123", "US", "New York", "3")

    def test_accented_place_is_queried(self):
        with patch.object(k, "search", return_value=self.places()[:1]) as search:
            k.place_constant("token", "123", "BR", "São Paulo")
            self.assertIn("São Paulo", search.call_args.args[-1])

    def test_corrupt_cache_refetches(self):
        args = SimpleNamespace(country="ZA", place=None, place_id=None, language="en", seed=["plumber"], url=[], keyword=[], limit=20, refresh=False)
        with tempfile.TemporaryDirectory() as directory:
            cached = Path(directory) / "cache.json"
            cached.write_text("broken json")
            with patch.object(k, "cache_file", return_value=cached), patch.object(k, "parse_args", return_value=args), patch.object(k, "load_config", return_value=("123", Path("fake-key"))), patch.object(k, "access_token", return_value="fake"), patch.object(k, "country_constant", return_value="geo"), patch.object(k, "language_constant", return_value="lang"), patch.object(k, "fetch_ideas", return_value=[]), patch.object(k, "currency_code", return_value="ZAR"), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(k.main(), 0)
            self.assertEqual(json.loads(cached.read_text())["currency_code"], "ZAR")

    def test_unique_place_still_resolves(self):
        with patch.object(k, "search", return_value=self.places()[:1]):
            self.assertEqual(k.place_constant("token", "123", "US", "New York")[0], "geoTargetConstants/1")

    def test_cli_rejects_multiple_urls_before_api(self):
        argv = ["script", "--country", "ZA", "--language", "en", "--url", "https://one.example", "--url", "https://two.example"]
        with patch.object(sys, "argv", argv), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                k.parse_args()
            self.assertEqual(error.exception.code, 2)

    def test_single_url_is_sent(self):
        with patch.object(k, "ads_request", return_value={"results": []}) as request:
            k.fetch_ideas("token", "123", language="lang", geo="geo", seeds=[], urls=["https://one.example"], limit=20)
            self.assertEqual(request.call_args.args[-1]["urlSeed"], {"url": "https://one.example"})

    def test_account_and_api_cache_isolation_and_same_account_reuse(self):
        args = SimpleNamespace(country="ZA", place=None, place_id=None, language="en", seed=["plumber"], url=[], keyword=[], limit=20, refresh=False)
        with tempfile.TemporaryDirectory() as directory, patch.object(k.Path, "home", return_value=Path(directory)), patch.object(k, "parse_args", return_value=args), patch.object(k, "load_config", return_value=("123", Path("fake-key"))) as config, patch.object(k, "access_token", return_value="fake") as token, patch.object(k, "country_constant", return_value="geo"), patch.object(k, "language_constant", return_value="lang"), patch.object(k, "fetch_ideas", return_value=[]), patch.object(k, "currency_code", return_value="ZAR"), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(k.main(), 0)
            self.assertEqual(k.main(), 0)
            self.assertEqual(token.call_count, 1)
            config.return_value = ("456", Path("fake-key"))
            self.assertEqual(k.main(), 0)
            self.assertEqual(token.call_count, 2)
            with patch.object(k, "API", "https://example.test/next-api"):
                self.assertEqual(k.main(), 0)
            self.assertEqual(token.call_count, 3)

    def test_explicit_location_id_has_own_cache(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(k.Path, "home", return_value=Path(directory)):
            self.assertNotEqual(k.cache_file({"place_id": "1"}), k.cache_file({"place_id": "2"}))

    def test_metrics_keep_missing_values_unknown(self):
        row = k.metric_row({"text": "niche service"})
        self.assertIsNone(row["avg_monthly_searches"])
        self.assertIsNone(row["low_top_of_page_bid"])

if __name__ == "__main__":
    unittest.main()
