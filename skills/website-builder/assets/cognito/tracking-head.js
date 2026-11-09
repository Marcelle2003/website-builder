/* Load in the public-site head before form embeds. See references/cognito-forms.md. */
(function (window) {
    'use strict';
    if (window.refreshCognitoTrackingPrefillPayload) return;

    var key = 'tracking_parameters';
    var lifetime = 90 * 24 * 60 * 60 * 1000;
    var memory = null;
    var fields = {
        Gclid: 'gclid', Gbraid: 'gbraid', Wbraid: 'wbraid',
        LeadSource: 'utm_source', UtmMedium: 'utm_medium',
        CampaignName: 'utm_campaign', AdsetName: 'utm_adset', AdName: 'utm_ad',
        UtmTerm: 'utm_term', UtmContent: 'utm_content',
        LandingPage: 'landing_page', UserAgent: 'user_agent'
    };

    function valid(value) {
        return value && typeof value === 'object' && !Array.isArray(value) &&
            typeof value.expiryTime === 'number' && Number.isFinite(value.expiryTime) &&
            value.expiryTime > Date.now();
    }

    function param(name) {
        var value;
        try { value = new URL(window.location.href).searchParams.get(name); } catch (error) { return null; }
        return value && value.trim() ? value.trim() : null;
    }

    function capture() {
        return {
            gclid: param('gclid'),
            gbraid: param('gbraid'),
            wbraid: param('wbraid'),
            utm_source: param('utm_source') || 'Website',
            utm_medium: param('utm_medium') || 'Form',
            utm_campaign: param('utm_campaign'),
            utm_adset: param('utm_adset'),
            utm_ad: param('utm_ad'),
            utm_term: param('utm_term'),
            utm_content: param('utm_content'),
            landing_page: window.location.href || null,
            user_agent: window.navigator.userAgent || null,
            expiryTime: Date.now() + lifetime
        };
    }

    function read() {
        try { return JSON.parse(window.localStorage.getItem(key)); } catch (error) { return null; }
    }

    function payloadFrom(token) {
        var payload = {};
        Object.keys(fields).forEach(function (field) {
            var value = token[fields[field]];
            payload[field] = typeof value === 'string' && value.trim() ? value.trim() : null;
        });
        payload.LeadSource = payload.LeadSource || 'Website';
        payload.UtmMedium = payload.UtmMedium || 'Form';
        return payload;
    }

    window.refreshCognitoTrackingPrefillPayload = function () {
        var token = read();
        if (!valid(token)) {
            try { window.localStorage.removeItem(key); } catch (error) { /* Storage may be blocked. */ }
            token = valid(memory) ? memory : capture();
            memory = token;
            try { window.localStorage.setItem(key, JSON.stringify(token)); } catch (error) { /* Keep this page usable. */ }
        } else {
            memory = token;
        }
        var payload = payloadFrom(token);
        window.__cognitoTrackingPrefill = payload;
        return payload;
    };

    window.refreshCognitoTrackingPrefillPayload();
})(window);
