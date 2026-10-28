'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assets = path.join(__dirname, '../skills/website-builder/assets/cognito');
const head = fs.readFileSync(path.join(assets, 'tracking-head.js'), 'utf8');
const footer = fs.readFileSync(path.join(assets, 'tracking-footer.js'), 'utf8');
const lifetime = 90 * 24 * 60 * 60 * 1000;
const plain = value => JSON.parse(JSON.stringify(value));
function page(options = {}) {
    let now = options.now || 1800000000000;
    const storage = options.storage || new Map();
    const timers = [];
    const calls = [];
    const window = {
        location: { href: options.url || 'https://example.test/' },
        navigator: { userAgent: 'test-browser' },
        localStorage: {
            getItem: key => { if (options.readBlocked) throw Error('blocked'); return storage.get(key) ?? null; },
            setItem: (key, value) => { if (options.writeBlocked) throw Error('quota'); storage.set(key, value); }
        },
        document: { querySelector: selector => options.elements?.includes(selector) ? {} : null },
        setTimeout: callback => timers.push(callback)
    };
    if (options.storageBlocked) Object.defineProperty(window, 'localStorage', { get() { throw Error('denied'); } });
    const context = vm.createContext({ window, URL, Date: { now: () => now } });
    return {
        window, storage, timers, calls,
        head: () => vm.runInContext(head, context),
        footer: () => vm.runInContext(footer, context),
        advance: amount => { now += amount; },
        flush: () => { let count = 0; while (timers.length) { assert.ok(count++ < 1000); timers.shift()(); } },
        sdk: () => { window.Cognito = { prefill: payload => calls.push(plain(payload)) }; }
    };
}

test('maps all twelve fields, decodes query values and stores exactly 90 days', () => {
    const p = page({url:'https://example.test/?gclid=g&gbraid=b&wbraid=w&utm_source=Search&utm_medium=CPC&utm_campaign=Camp+One&utm_adset=set&utm_ad=ad&utm_term=a%26b&utm_content=hero'});
    p.head();
    assert.deepEqual(plain(p.window.__cognitoTrackingPrefill), {
        Gclid:'g',Gbraid:'b',Wbraid:'w',LeadSource:'Search',UtmMedium:'CPC',CampaignName:'Camp One',
        AdsetName:'set',AdName:'ad',UtmTerm:'a&b',UtmContent:'hero',
        LandingPage:p.window.location.href,UserAgent:'test-browser'
    });
    assert.equal(JSON.parse(p.storage.get('tracking_parameters')).expiryTime,1800000000000+lifetime);
});

test('direct first touch uses defaults and survives later campaigns without extending expiry', () => {
    const first=page();first.head();const token=first.storage.get('tracking_parameters');
    const next=page({storage:first.storage,now:1800000001000,url:'https://example.test/contact?gclid=later&utm_source=later'});next.head();
    assert.equal(next.window.__cognitoTrackingPrefill.LeadSource,'Website');
    assert.equal(next.window.__cognitoTrackingPrefill.UtmMedium,'Form');
    assert.equal(next.window.__cognitoTrackingPrefill.Gclid,null);
    assert.equal(next.window.__cognitoTrackingPrefill.LandingPage,'https://example.test/');
    assert.equal(next.storage.get('tracking_parameters'),token);
});

test('expired attribution refreshes at the exact boundary', () => {
    const p=page({url:'https://example.test/?gclid=old'});p.head();
    p.advance(lifetime);p.window.location.href='https://example.test/new?gclid=new';
    assert.equal(p.window.refreshCognitoTrackingPrefillPayload().Gclid,'new');
});

test('invalid JSON, nonobjects and missing/invalid expiry are replaced', () => {
    for (const token of ['{','null','[]','false','"text"','{}','{"expiryTime":"later"}','{"expiryTime":0}']) {
        const p=page({storage:new Map([['tracking_parameters',token]]),url:'https://example.test/?gclid=recovered'});
        p.head();assert.equal(p.window.__cognitoTrackingPrefill.Gclid,'recovered');
        assert.equal(JSON.parse(p.storage.get('tracking_parameters')).gclid,'recovered');
    }
});

test('existing supplied-script tokens remain compatible and values are not treated as code', () => {
    const raw={gclid:'<script>alert(1)</script>',utm_source:'original',expiryTime:1800000000000+lifetime,landing_page:'https://example.test/first'};
    const p=page({storage:new Map([['tracking_parameters',JSON.stringify(raw)]])});p.head();
    assert.equal(p.window.__cognitoTrackingPrefill.Gclid,raw.gclid);
    assert.equal(p.window.__cognitoTrackingPrefill.LeadSource,'original');
    assert.equal(p.window.__cognitoTrackingPrefill.UtmMedium,'Form');
    assert.equal(p.window.__cognitoTrackingPrefill.LandingPage,raw.landing_page);
});

test('storage getter, read and write failures retain usable in-page first-touch payload', () => {
    for(const failure of [{storageBlocked:true},{readBlocked:true,writeBlocked:true},{writeBlocked:true}]) {
        const p=page({...failure,url:'https://example.test/?gclid=first'});p.head();
        p.window.location.href='https://example.test/?gclid=second';
        assert.equal(p.window.refreshCognitoTrackingPrefillPayload().Gclid,'first');
    }
});

test('malformed percent encoding does not crash tracking', () => {
    const p=page({url:'https://example.test/?utm_campaign=%E0%A4%A'});
    assert.doesNotThrow(p.head);assert.equal(typeof p.window.__cognitoTrackingPrefill.CampaignName,'string');
});

test('no configured form means no polling or SDK calls', () => {
    const p=page();p.head();p.sdk();p.footer();
    assert.equal(p.calls.length,0);assert.equal(p.timers.length,0);
});

test('late SDK prefills once and repeat initialization preserves visitor edits', () => {
    const p=page();p.head();p.window.__cognitoTrackingTargets=[{key:'contact'}];p.footer();
    assert.equal(p.window.__cognitoTrackingStatus.contact,'pending');
    p.sdk();p.flush();p.footer();p.window.prefillCognitoTracking([{key:'contact'}]);
    assert.equal(p.calls.length,1);assert.equal(p.window.__cognitoTrackingStatus.contact,'dispatched');
});

test('footer waits for the head payload if loaded out of order', () => {
    const p=page();p.sdk();p.window.__cognitoTrackingTargets=[{key:'contact'}];p.footer();
    p.head();p.flush();assert.equal(p.calls.length,1);
});

test('SDK wait is bounded; lazy initialization can explicitly retry afterward', () => {
    const p=page();p.head();p.window.__cognitoTrackingTargets=[{key:'lazy'}];p.footer();p.flush();
    assert.equal(p.window.__cognitoTrackingStatus.lazy,'unavailable');assert.equal(p.timers.length,0);
    p.sdk();p.window.prefillCognitoTracking([{key:'lazy'}]);assert.equal(p.calls.length,1);
});

test('multiple targets use the actual form IDs and wrappers and deduplicate each instance', () => {
    const p=page({elements:['#contact','#quote']});p.head();
    p.window.Cognito={mount:(id,selector)=>({prefill:payload=>p.calls.push({id,selector,payload:plain(payload)})})};
    const targets=[{key:'one',formId:'9',selector:'#contact'},{key:'two',formId:'10',selector:'#quote'}];
    p.window.__cognitoTrackingTargets=targets;p.footer();p.window.prefillCognitoTracking(targets);
    assert.deepEqual(p.calls.map(({id,selector})=>[id,selector]),[['9','#contact'],['10','#quote']]);
});

test('an unavailable wrapper times out without mounting to another form', () => {
    const p=page();p.head();p.window.Cognito={mount:()=>{throw Error('must not mount');}};
    p.window.__cognitoTrackingTargets=[{key:'missing',formId:'9',selector:'#absent'}];p.footer();p.flush();
    assert.equal(p.window.__cognitoTrackingStatus.missing,'unavailable');
});

test('SDK errors are reported without an automatic retry storm', () => {
    const p=page();p.head();p.window.Cognito={prefill:()=>{throw Error('not accepted');}};
    p.window.__cognitoTrackingTargets=[{key:'broken'}];p.footer();
    assert.equal(p.window.__cognitoTrackingStatus.broken,'error');assert.equal(p.timers.length,0);
});

test('partial multi-form configuration does not fall back to a global prefill', () => {
    const p=page();p.head();p.sdk();
    p.window.__cognitoTrackingTargets=[{key:'partial',formId:'9'}];p.footer();
    assert.equal(p.calls.length,0);assert.equal(p.window.__cognitoTrackingStatus.partial,'error');
});

test('invalid CSS selector is reported without crashing the page', () => {
    const p=page();p.head();p.window.document.querySelector=()=>{throw Error('syntax');};
    p.window.__cognitoTrackingTargets=[{key:'invalid',formId:'9',selector:'['}];
    assert.doesNotThrow(p.footer);assert.equal(p.window.__cognitoTrackingStatus.invalid,'error');
});
