# 2026-07-29 — Light graphics across marketing pages

## Summary

All content diagrams on public pages now use light mist/white SVG variants (navy/teal on light). Homepage help cards and enterprise diagram, plus the diagnostics outputs panel, were still on dark assets; those now point at `-light.svg` files. CSS/JS/img cache query bumped to `?v=light1`.

## Src changes (old → new)

| Page | Old | New |
|------|-----|-----|
| index.html | `help-diagnostics.svg` | `help-diagnostics-light.svg` |
| index.html | `help-architecture.svg` | `help-architecture-light.svg` |
| index.html | `help-implementation.svg` | `help-implementation-light.svg` |
| index.html | `enterprise-operations.svg` | `enterprise-operations-light.svg` |
| diagnostics.html | `diagnostics-outputs-panel.svg` | `diagnostics-outputs-panel-light.svg` |
| enhancements.css (unused tile CSS) | `architecture-diagram.svg` | `architecture-diagram-light.svg` |

Other marketing pages already referenced `*-light.svg` hero/diagram assets; those gained `?v=light1` for cache bust only.

## New light assets

- `assets/visuals/help-implementation-light.svg`
- `assets/visuals/enterprise-operations-light.svg`
- `assets/visuals/diagnostics-outputs-panel-light.svg`

## Intentional dark leftovers

- Footer logo (`prime-ai-logo-nav.svg`): light-on-dark chrome on the dark footer band.
- Favicon / app icon: brand chrome, not content diagrams.
- Founder photos: photos, unchanged.
- Unused CSS tile backgrounds (`tile-*.svg`, `data-dictionary-mockup.svg`, `timeline-10-week.svg`, `hero-manufacturing-texture.svg`): not referenced by current public HTML (legacy lifecycle/sector tile styles). Files remain dark; no live page shows them.
- `mes-ai-integration-roadmap.png`: dark PNG on disk; not referenced by live HTML (methodology uses the native light roadmap widget).

## Cache

- Asset query `?v=light1` on CSS/JS across pages; visual img `src` query strings match.
- `scripts/unify_site_chrome.py` `CSS_VERSION = "light1"`.
