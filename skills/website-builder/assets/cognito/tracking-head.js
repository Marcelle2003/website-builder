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

    function capture() {
        var params = new URL(window.location.href).searchParams;
        var token = {};
        Object.keys(fields).forEach(function (field) {
            var source = fields[field];
            token[source] = params.get(source) || null;
        });
        token.utm_source = token.utm_source || 'Website';
        token.utm_medium = token.utm_medium || 'Form';
        token.landing_page = window.location.href || null;
        token.user_agent = window.navigator.userAgent || null;
        token.expiryTime = Date.now() + lifetime;
        return token;
    }

    window.refreshCognitoTrackingPrefillPayload = function () {
        var token = null;
        try { token = JSON.parse(window.localStorage.getItem(key)); } catch (error) { /* Storage may be blocked. */ }
        if (!valid(token)) token = valid(memory) ? memory : capture();
        memory = token;
        try {
            // Preserve the first touch and original expiry across pages; no sliding renewal.
            window.localStorage.setItem(key, JSON.stringify(token));
        } catch (error) { /* Keep this page usable with the in-memory payload. */ }
        var payload = {};
        Object.keys(fields).forEach(function (field) {
            var value = token[fields[field]];
            payload[field] = typeof value === 'string' && value ? value : null;
        });
        payload.LeadSource = payload.LeadSource || 'Website';
        payload.UtmMedium = payload.UtmMedium || 'Form';
        window.__cognitoTrackingPrefill = payload;
        return payload;
    };

    window.refreshCognitoTrackingPrefillPayload();
})(window);
