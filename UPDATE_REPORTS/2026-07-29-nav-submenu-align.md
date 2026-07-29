# 2026-07-29 — Mobile Services submenu left-align

## Summary

On mobile (drawer nav below 1180px), the Services submenu items were centered because `.nav-links li { align-items: center }` shrink-wrapped `.nav-sub`. CSS now stretches the parent item and left-aligns submenu links.

## Changes

- **CSS:** `@media (max-width: 1179px)` — `.nav-links > .nav-item-has-sub` uses `align-items: stretch`; submenu full-width, left text/padding aligned with content pad.
- **Cache bust:** asset query `?v=nav3` on CSS/JS across pages; `CSS_VERSION` in `unify_site_chrome.py`.

## Files

- `assets/enhancements.css`
- HTML pages (`?v=nav3`)
- `scripts/unify_site_chrome.py`
