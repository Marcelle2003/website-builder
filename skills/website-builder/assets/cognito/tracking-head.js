/* Load in the public-site head before form embeds. See references/cognito-forms.md. */
(function (window) {
    'use strict';
    if (window.refreshCognitoTrackingPrefillPayload) return;

    var clickKey = 'tracking_parameters';
    var utmKey = 'utm_parameters';
    var clickLifetime = 90 * 24 * 60 * 60 * 1000;
    var utmLifetime = 30 * 24 * 60 * 60 * 1000;
    var clickMemory = null;
    var utmMemory = null;
    var utmNames = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_adset', 'utm_ad', 'utm_term', 'utm_content'];
    var clickMap = {
        Gclid: 'gclid', Gbraid: 'gbraid', Wbraid: 'wbraid',
        LandingPage: 'landing_page', UserAgent: 'user_agent'
    };
    var utmMap = {
        LeadSource: 'utm_source', UtmMedium: 'utm_medium',
        CampaignName: 'utm_campaign', AdsetName: 'utm_adset', AdName: 'utm_ad',
        UtmTerm: 'utm_term', UtmContent: 'utm_content'
    };

    function valid(value) {
        return value && typeof value === 'object' && !Array.isArray(value) &&
            typeof value.expiryTime === 'number' && Number.isFinite(value.expiryTime) &&
            value.expiryTime > Date.now();
    }

    function read(storageKey) {
        try { return JSON.parse(window.localStorage.getItem(storageKey)); } catch (error) { return null; }
    }

    function write(storageKey, value) {
        try { window.localStorage.setItem(storageKey, JSON.stringify(value)); } catch (error) { /* Keep this page usable. */ }
    }

    function remove(storageKey) {
        try { window.localStorage.removeItem(storageKey); } catch (error) { /* Storage may be blocked. */ }
    }

    function param(name) {
        var value;
        try { value = new URL(window.location.href).searchParams.get(name); } catch (error) { return null; }
        return value && value.trim() ? value.trim() : null;
    }

    function hasNewUtm() {
        return utmNames.some(function (name) { return param(name) !== null; });
    }

    function freshUtm() {
        return {
            utm_source: param('utm_source') || 'Website',
            utm_medium: param('utm_medium') || 'Form',
            utm_campaign: param('utm_campaign'),
            utm_adset: param('utm_adset'),
            utm_ad: param('utm_ad'),
            utm_term: param('utm_term'),
            utm_content: param('utm_content'),
            expiryTime: Date.now() + utmLifetime
        };
    }

    function freshClick() {
        return {
            gclid: param('gclid'),
            gbraid: param('gbraid'),
            wbraid: param('wbraid'),
            landing_page: window.location.href || null,
            user_agent: window.navigator.userAgent || null,
            expiryTime: Date.now() + clickLifetime
        };
    }

    function legacyUtm(click) {
        if (!valid(click)) return null;
        return {
            utm_source: click.utm_source || 'Website',
            utm_medium: click.utm_medium || 'Form',
            utm_campaign: click.utm_campaign || null,
            utm_adset: click.utm_adset || null,
            utm_ad: click.utm_ad || null,
            utm_term: click.utm_term || null,
            utm_content: click.utm_content || null,
            expiryTime: click.expiryTime
        };
    }

    function loadUtm() {
        var present = false;
        var stored = null;
        try {
            present = window.localStorage.getItem(utmKey) !== null;
            stored = read(utmKey);
        } catch (error) {
            present = false;
            stored = null;
        }
        if (present && !valid(stored)) {
            remove(utmKey);
            stored = null;
        } else if (!present) {
            stored = legacyUtm(read(clickKey));
        }
        if (!valid(stored) && valid(utmMemory)) stored = utmMemory;
        if (valid(stored) && !hasNewUtm()) return stored;
        return freshUtm();
    }

    function loadClick() {
        var stored = read(clickKey);
        if (!valid(stored)) {
            remove(clickKey);
            stored = valid(clickMemory) ? clickMemory : freshClick();
        }
        return stored;
    }

    function text(value) {
        return typeof value === 'string' && value.trim() ? value.trim() : null;
    }

    window.refreshCognitoTrackingPrefillPayload = function () {
        var utm = loadUtm();
        var click = loadClick();
        utmMemory = utm;
        clickMemory = click;
        write(utmKey, utm);
        write(clickKey, click);
        var payload = {};
        Object.keys(utmMap).forEach(function (field) { payload[field] = text(utm[utmMap[field]]); });
        Object.keys(clickMap).forEach(function (field) { payload[field] = text(click[clickMap[field]]); });
        payload.LeadSource = payload.LeadSource || 'Website';
        payload.UtmMedium = payload.UtmMedium || 'Form';
        window.__cognitoTrackingPrefill = payload;
        return payload;
    };

    window.refreshCognitoTrackingPrefillPayload();
})(window);
