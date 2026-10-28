/* Set __cognitoTrackingTargets before loading; an empty list does no work. */
(function (window) {
    'use strict';
    if (window.prefillCognitoTracking) return;
    var states = Object.create(null);
    window.__cognitoTrackingStatus = states;

    window.prefillCognitoTracking = function (targets) {
        (targets || []).forEach(function (target) {
            if (!target || typeof target.key !== 'string' || !target.key) return;
            if (states[target.key] === 'pending' || states[target.key] === 'dispatched') return;
            var mounted = target.formId !== undefined || target.selector !== undefined;
            if (mounted && (typeof target.formId !== 'string' || !target.formId ||
                typeof target.selector !== 'string' || !target.selector)) {
                states[target.key] = 'error';
                return;
            }
            var attempts = 0;
            states[target.key] = 'pending';
            function attempt() {
                var cognito = window.Cognito;
                var ready = cognito && (mounted ? typeof cognito.mount === 'function' : typeof cognito.prefill === 'function');
                if (mounted) {
                    try {
                        if (!window.document.querySelector(target.selector)) ready = false;
                    } catch (error) {
                        states[target.key] = 'error';
                        return;
                    }
                }
                if (ready && typeof window.refreshCognitoTrackingPrefillPayload === 'function') {
                    try {
                        var payload = window.refreshCognitoTrackingPrefillPayload();
                        var form = mounted ? cognito.mount(target.formId, target.selector) : cognito;
                        form.prefill(payload);
                        // A dispatch is not proof that fields rendered or an entry was saved.
                        states[target.key] = 'dispatched';
                    } catch (error) {
                        states[target.key] = 'error';
                    }
                    return;
                }
                attempts += 1;
                if (attempts < 60) window.setTimeout(attempt, 250);
                else states[target.key] = 'unavailable';
            }
            attempt();
        });
    };

    window.prefillCognitoTracking(window.__cognitoTrackingTargets);
})(window);
