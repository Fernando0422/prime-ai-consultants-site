# 2026-07-29 — Founders intro line breaks

## Summary

Forced intentional line breaks on the About Us “The founders” intro so the headline and body read as short stacked lines instead of one wrapped paragraph. Matched the homepage founders headline break for consistency. No copy rewrite; no em dashes; cache query left at `wrap1` (HTML-only change).

## Changes

| Page | Change |
|------|--------|
| company.html | h2: break after “Father and son.”; lede: one sentence per line via `<br />` |
| index.html | Same h2 break on founders intro title |
