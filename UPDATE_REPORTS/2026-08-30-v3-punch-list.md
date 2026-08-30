# 2026-08-30 — V3 punch list: methodology CTA + contact dropdown

## Summary

Worked the V3 punch list from the ux-web-critique skill against the current site. The redesign had already resolved most items; two needed real fixes, both applied and verified.

## Fixed

1. **End-of-methodology CTA is now a full-width dark section.** The methodology final CTA was `section-mist` (light), inconsistent with the dark final-CTA panels on the homepage and Services. Changed to `section section-dark final-cta-section meth-final` and updated the meth-final text colors in `assets/enhancements.min.css` so the heading, lede, and secondary button read correctly on dark:
   - `.page-methodology .meth-final-copy .h-h2` color → `#fff`
   - `.page-methodology .meth-final-copy .lede` color → `rgba(255,255,255,0.86)`
   - `.page-methodology .meth-final .btn-secondary` → white outline on transparent, light hover state

2. **Contact form now has a real MES/ERP platform dropdown.** Replaced the free-text "Primary system" input with a `select` (name preserved as `primarySystem`, so the mailto GET payload is unchanged). Options: Camstar, SAP ME/MII, Siemens Opcenter, FactoryTalk, SAP ECC, Oracle MES, Other, Not sure. Uses the existing `.form-select` styling; the form JS reads `fieldVal("primarySystem")` which works identically for selects.

## Already resolved by the 2026-08 redesign (verified, no change needed)

- Typography consistency: h1/h2/h3 all `font-weight:700`, same family, `text-wrap:balance`; buttons normalized via shared `.btn` variables. Legal-page h2s styled by `.legal-body h2`.
- Service-card heading weights: cards use `.h-h3`, page headings `.h-h2`, both weight 700 (intended hierarchy only).
- MES "three horizons" headline: no longer exists on ai-mes.html (redesigned away).
- Homepage problem-card headline wrap: old headline removed; current cards are short titles.
- Teal hyperlinks in body text: global `a { color: inherit }`; methodology has no body-text links (all anchors are nav/CTA/footer).
- About operating-principles grid: `.about-pillar-grid` is 2-column at ≥800px, 4 cards (2x2).
- About origin story alignment: body text left-aligned; only section *heads* are centered by design.
- Footer logo: footer partial already uses the SVG wafer-mark logo (`assets/prime-ai-logo-nav.svg`).

## Cache

- `enhancements.min.css?v=heroctr1` → `v=heroctr2` in all 13 HTML pages.

## Note

Legacy build scripts (`scripts/unify_site_chrome.py`, `scripts/copy_v2/shell.py`) still reference old CSS filenames/version tokens (`enhancements.css`, `wrap1`, `flow12`); they are not used by the current hand-edited, Vercel-deployed pages and were left untouched.
