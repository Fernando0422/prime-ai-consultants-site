# 2026-07-29 — Widow/orphan text wrap fixes

## Summary

Fixed one-word hang lines on key heroes and CTAs by widening constrained `max-width` columns slightly, adding non-breaking spaces between last two words of short phrases, and applying `text-wrap: pretty` on interior heroes/leads. Converted the methodology overview SVG's dark step-03 (Govern) detail panel to the same light treatment as Discover/Define. Cache query bumped to `?v=wrap1`.

## Orphans fixed (page + phrase)

| Page | Phrase |
|------|--------|
| methodology.html | next step. / don't start. |
| ai-erp.html | written down. / answer differently. |
| company.html | On purpose. |
| diagnostics.html | build on it. |
| services.html | written down. / a solution. |
| ai-mes.html | find them. / answer consistently. |
| ai-crm.html | touches it. / On purpose. / for both. |
| contact.html | the question. |

## CSS / HTML

- Widened page-specific hero/CTA `ch`/`rem` caps (methodology, ERP/CRM, about, diagnostics, MES, contact).
- `text-wrap: pretty` on `.page-interior` hero h1/lede and page-specific hero/final headings.
- `&nbsp;` between last two words of the phrases above.
- `methodology-overview-light.svg`: third detail panel fill `#0A0F1E` → white + light placeholder bars (matches panels 1–2).

## Cache

- Asset query `?v=wrap1` on CSS/JS across pages; methodology overview img `?v=wrap1`.
- `CSS_VERSION` in `unify_site_chrome.py` → `wrap1`.
