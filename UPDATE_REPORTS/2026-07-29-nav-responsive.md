# 2026-07-29 — Responsive nav overflow fix

## Summary

Mid-width viewports (roughly laptop / small desktop) overflowed the horizontal nav. Fluid breakpoints replace the old 920/921px toggle so the hamburger appears earlier and the full link row compresses before it wraps.

## Changes

- **Hamburger / drawer:** below **1180px** (`max-width: 1179px` / `min-width: 1180px` desktop MQ in CSS + `site.js`).
- **Compress band (1180–1399px):** smaller logo, tighter padding/gaps, shorter link labels via “Diagnostics” + `aria-label`, hide nav CTA until 1400px+.
- **1400px+:** restore fuller spacing and link size.
- **Cache bust:** asset query `?v=nav2` on CSS/JS across pages; `CSS_VERSION` in `unify_site_chrome.py`.

## Files

- `assets/enhancements.css`, `assets/styles.css`, `assets/site.js`
- HTML pages (nav label + `?v=nav2`)
- `scripts/unify_site_chrome.py`, `scripts/copy_v2/shell.py`
