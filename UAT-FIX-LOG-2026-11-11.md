# UAT fix log, staging, 2026-11-11

Branch: `staging-qa-2026-11-11` (repo Fernando0422/prime-ai-consultants-site).
Base commit: 0a4e934cd62e10c4a81b036382e76e06d2b145e7.
Staging preview: https://prime-ai-consultants-site-1mk0kl06n.vercel.app
Main/production was not touched. No emails sent, no clients contacted.

## Canonical contact (P0.3)

One phone, one email, one location, one nav style, one form behavior across all
5 pages.

- Phone: **661-779-5568** (tel:+16617795568). Fernando's published Prime number.
  It was already on the newest homepage, Law, and Local pages and in the live
  homepage schema. Replaced (805) 216-4651 on Manufacturing and Manufacturing
  Industries (3 tel links and 3 display instances on Manufacturing; 3 tel and
  4 display on Manufacturing Industries).
- Email: **Fernando@primeaiconsultants.com**. It was already the mailto
  destination of the QA contact forms and on the newest homepage, Law, and
  Local pages. Replaced hello@primeaiconsultants.com (7 instances on each of
  Manufacturing and Manufacturing Industries, including form mailto targets
  and status text). The live site is split on this: the homepage schema lists
  the 661 number, while /contact.html still lists hello@ and the (805) number.
  Fernando@ was chosen because it is the address the newest pages and the QA
  forms already use. If hello@ turns out to be the monitored Prime inbox, the
  swap back is a one-line change per form.
- Location: **Santa Clarita, California**. Replaced "Greater Los Angeles,
  California" (2 instances on each manufacturing page). Matches the live
  homepage schema and the homepage footer.
- Antonio's direct email antonio.rojas@primeaiconsultants.com was kept where
  it appears as Antonio's personal contact, not as general contact.
- Nav style: one desktop nav with the same structure on all pages; dropdown
  gaps fixed (see P0.1). Form behavior: every page with a form now uses a
  mailto anchor click (no page navigation) plus an inline confirmation that
  the page scrolls to. Law has no form, only call/email/text links, unchanged.

## Fixes

### P0.1 Industries dropdown (index.html)
- Submenu top changed from `calc(100% + 10px)` to `100%`, and an invisible
  14px bridge (`li.nav-item::after`) now covers the strip between trigger and
  panel, so moving straight down no longer drops the menu. No close timer.
- Removed the duplicate "Manufacturing Industries" entry from the Industries
  submenu. It stays linked from the footer and from the Manufacturing page nav.
- Same gap fix on the Applications dropdowns: manufacturing.html
  (`calc(100% + 8px)` to `100%`, 10px bridge on `.nav-has-dropdown`) and
  manufacturing-industries.html (`calc(100% + 6px)` to `100%`, 10px bridge on
  `.nav-links>li`).

### P0.2 Nav pill / active state
- index.html: added click handling plus a scroll spy. Clicking Diagnostics,
  Methodology, About, Contact, or Industries moves the teal pill at once;
  scrolling updates it; Home is active at the top. Previously the pill stayed
  on Home and there was no scroll spy at all.
- manufacturing.html: fixed two pills at once. The "Applications overview"
  dropdown link no longer also goes active when the Applications toggle is
  active, and Home (index.html) is now active at the top of the page.
- manufacturing-industries.html: added click handling plus a scroll spy
  (previously Industries was hard-coded active). Also removed the Methodology
  and Services nav links (desktop and mobile menu): those sections do not
  exist on this page, so the links went nowhere.
- law.html: added click handling plus a scroll spy (previously "Law Firms"
  was hard-coded active).
- local-businesses.html: added click handling plus a scroll spy (previously
  "Local Businesses" was hard-coded active).

### P0.3 Reconciled contact/nav/form (all 5 pages)
- See Canonical contact above. Files: manufacturing.html,
  manufacturing-industries.html (contact values replaced);
  index.html, law.html, local-businesses.html (already canonical, no contact
  changes needed).
- Local form now matches the Name + Email only rule (see P1, local form).

### P0.4 Mobile at 390px
- Checked with headless Chromium at 390x844 on local files, plus a
  scrollWidth probe per page. Found two pre-existing overflows, both fixed:
  - index.html: the "Email Fernando@primeaiconsultants.com" button is one
    unbreakable token and forced the contact grid item to 377px wide against a
    335px track (document scrollWidth 397). Fixed with
    `overflow-wrap:anywhere` on `.contact-actions .btn` and `min-width:0` on
    `.contact-copy`.
  - law.html: the header CTA button (226px) plus brand plus hamburger
    overflowed to 453px. Fixed by hiding the header CTA button below 640px,
    the same rule the manufacturing pages already use.
- After fixes, all 5 pages report document scrollWidth 375 at a 390px
  viewport (375 is the layout width once the 15px classic scrollbar is
  accounted for), with no element wider than the viewport. Mobile screenshots
  at 390px confirm clean headers and headings on index, manufacturing, law,
  and local-businesses, with no clipped headings or broken images.

### P1.5 Anchor scroll offset (all 5 pages)
- Added `html{scroll-padding-top:110px}` and
  `section[id]{scroll-margin-top:110px}` so anchor jumps land below the
  sticky header instead of under it.

### P1.6 Manufacturing Industries header button
- Added `white-space:nowrap` to `.nav-cta .btn` on
  manufacturing-industries.html and manufacturing.html, so "Discuss your
  environment" no longer wraps to 3 lines at desktop width.

### P1.7 Home form stays on confirmation (index.html)
- Form submit no longer sets `window.location.href` to the mailto URL (that
  navigated the page away and it reloaded at the top). It now creates a
  temporary anchor, clicks it to open the mail app, then unhides the
  confirmation and scrolls it into view with focus.

### P1.8 Home form duplicate "Your industry" field (index.html)
- Root cause: the Other write-in field was always visible. `.form-field` sets
  `display:flex`, which overrides the browser default `[hidden]{display:none}`.
  Added a global `[hidden]{display:none!important}` rule (all 5 pages), so
  the Other write-in only appears when Other is selected. The dropdown plus
  Other write-in are kept; the always-visible duplicate free-text field is
  gone. The same rule also fixes the hidden Other field on manufacturing.html.

### P2.9 Footer Home link
- Added a Home link as the first footer link on index.html. Law, Local, and
  Manufacturing Industries footers already had one; manufacturing.html
  already had one. Verified present on all 5 pages.

### P2.10 Vercel Toolbar
- Not fixable in code. The toolbar is a Vercel dashboard setting, not a
  vercel.json key: project/team Settings, General, Vercel Toolbar, set
  Pre-Production (and Production) to Off. No config change was made, and no
  unverified `"toolbar": false` key was added to vercel.json. Note the toolbar
  only appears to logged-in team members, not to public visitors.

### P2.11 Deduplicated repeated headings (index.html)
- The Methodology principles cards repeated the Six commitments headings
  word for word. The commitments keep "You own everything" and "Additive,
  never a replacement". The principles cards are now "You keep everything we
  build" and "Add to what works", with their body copy unchanged.
- Local Businesses was checked and left alone: "You own everything" appears
  there once as a principles heading, once as a FAQ question, and once in the
  FAQ answer/JSON-LD, which is not a repeated heading.

## Local form (local-businesses.html)
- The audit form had `action="#"` and no submit handler, so submitting
  reloaded the page at the top. It now has a mailto handler matching the
  homepage: opens the mail app to Fernando@primeaiconsultants.com, shows an
  inline confirmation, and scrolls to it.
- Business name and Phone are no longer required (only Name and Email are),
  labelled "(optional)", matching the form rule decided 2026-11-11.

## Verification done before push (local files, not live staging)
- All inline scripts pass `node --check` (6 scripts across 5 pages).
- No `hello@primeaiconsultants.com`, `(805)`, or `Greater Los Angeles` remains
  in any of the 5 pages. Phone 661-779-5568, email
  Fernando@primeaiconsultants.com, and Santa Clarita, California are present
  on every page.
- Mobile 390px scrollWidth probe: all 5 pages 375, no overflow. Screenshots
  reviewed for index, manufacturing, law, local-businesses.
- Not yet verified: the fixes on the live staging URL after the Vercel
  rebuild (dropdown hover behavior, nav pill movement on click/scroll, form
  submit staying on the confirmation, anchor offset in a real browser).
  Those need a rendered-browser re-check against the live staging link.
  Nothing in this log should be read as live-verified until that re-check
  is done.

## We-voice rewrite (2026-11-11, staging only)
- User request: homepage copy said "Prime" too much; change third-person "Prime" to first-person "We".
- Applied to all 5 pages (index.html, manufacturing.html, law.html, local-businesses.html, manufacturing-industries.html), body copy only, by text-node rewrite; script/style/title, JSON-LD, meta, aria-labels, and CSS comments untouched.
- Examples:
  - "Prime can help" -> "We can help"; "Prime is a consultancy. Businesses hire Prime to find..." -> "We're a consultancy. Businesses hire us to find..."
  - "Prime comes in, maps how the work and the data actually move" -> "We come in, map how the work and the data actually move"
  - "Prime goes in and meets..." -> "We go in and meet..." (verb agreement fixed: "meets/maps" -> "meet/map")
  - "Prime reviews your Google reviews" -> "We review your Google reviews"; "Prime also asks AI..." -> "We also ask AI..."
  - "Everything else helps Prime come to the first conversation prepared." -> "Everything else helps us come to the first conversation prepared."
  - "If a build is not worth doing, Prime says so" -> "If a build is not worth doing, we say so"
  - "Prime is based in the Santa Clarita Valley." -> "We're based in the Santa Clarita Valley."
  - Headings: "Who Prime is" -> "Who we are"; "How Prime works" -> "How we work"; "About Prime" -> "About us"; "What Prime can provide" -> "What we can provide"
- Kept unchanged: header/logo "Prime AI CONSULTANTS", footer "Prime AI Consultants · Santa Clarita, California" and "© 2026 Prime AI Consultants LLC. All rights reserved.", product name "Prime Diagnostics", founders' "co-founded Prime" / "At Prime he leads..." (firm as entity, in bios), law bio "Antonio leads governance and review at Prime", and the legal disclaimer "Prime claims no partnership..." on manufacturing.html.
- Visible-text "Prime" remaining after the rewrite is only those kept cases above (plus "Prime AI" in the logo). JSON-LD/meta still name the organisation as Prime AI Consultants, as schema requires.
- Facts, prices (free audit / free diagnostic), phone 661-779-5568, email Fernando@primeaiconsultants.com, first-step names, scores/proof points, and all UAT fixes already in the assembly (dropdown, nav pill, canonical contact, scroll offset, form behaviour, mobile fixes) were not changed.
- Verification (local files only): all 5 files parse as HTML; no "We + third-person -s verb" remains in visible text; sample converted sentences read cleanly. Live staging revalidation still required after push + Vercel rebuild — not yet done.

## Industries nav hover: label + chevron as one control (2026-11-11, staging only)
- User report (with screenshots): on the homepage nav, hovering INDUSTRIES highlighted the text and the chevron separately — one screenshot showed the chevron in its own grey pill with the text unhighlighted, the other showed the text in a grey pill with the chevron separate.
- Root cause (index.html): the desktop trigger was two sibling elements — `<a id="industries-link">Industries</a>` with its own hover pill, and a separate `<button id="industries-toggle">` chevron with its own hover pill.
- Fix (index.html only): merged them into a single anchor control — `<a href="#industries" class="nav-industries-control" id="industries-toggle" aria-haspopup="true" aria-expanded="false" aria-controls="industries-submenu">Industries <span class="chev">▾</span></a>`. One hover state, one active pill (scroll-spy already targets this anchor via `href="#industries"`), one focus state. Added CSS so hovering/focusing anywhere on the item — label, chevron, or while the cursor is in the submenu — highlights the whole trigger (`.nav-item:hover > .nav-industries-control`, `:focus-within`, `.is-open`).
- Click behaviour: first click/tap opens the submenu (preventDefault); a second click while open follows the link to #industries. `aria-expanded` is synced on click and on mouseenter/mouseleave. The earlier unified-hover fix is kept: the 14px invisible bridge (`.nav-item::after`) and the hover-opens-submenu rule are untouched, so moving from the trigger down into the panel keeps it open.
- Destinations unchanged: Industries overview (#industries), Services for Manufacturers, Services for Legal Professionals, Services for Local Businesses.
- Mobile menu row (separate link + toggle button) left as-is — no hover on touch, and merging it would change tap-to-expand vs navigate behaviour.
- No copy, facts, phone, email, or We-voice wording changed. law.html not touched (parallel Law-nav task).
- Sync check before push: the parallel Law-nav push had landed first as abf9bc22 (on top of 9bfe1ea7). Verified local law.html blob SHA (0837c7d0…) byte-matches remote law.html at the new head, so no divergence; this push covers index.html + this log only.
- Verification (local files only): index.html parses; single unified trigger confirmed in the DOM, no `industries-link` / `nav-sub-toggle` / `nav-industries-link` remnants on desktop; submenu hrefs unchanged; bridge + hover-open rules present; inline script passes `node --check`. Live staging revalidation still required after push + Vercel rebuild — not yet done.

## Law nav: remove Manufacturing / Local Businesses from top nav (2026-11-11, staging only)
- User request (with screenshot): on the law page, remove Manufacturing and Local Businesses from the nav so legal professionals aren't confused.
- law.html only: removed the two desktop-nav items `<li><a href="manufacturing.html">Manufacturing</a></li>` and `<li><a href="local-businesses.html">Local Businesses</a></li>` from `.nav-links`. No other page touched.
- Mobile menu: checked — it never contained Manufacturing / Local Businesses (only What we handle, Where firms lose, What we do, Questions, About us, Call), so nothing to remove there.
- Kept unchanged, as instructed: footer links (Manufacturing, Local businesses), the body cross-link "Our work in manufacturing and operations" (link-row), and the footer note mentioning manufacturers and local businesses. All other nav items kept: Law Firms (active), Home, Where Firms Lose, What We Do, Questions, About, plus the GET YOUR FREE DIAGNOSTIC button.
- No copy, facts, phone, email, or We-voice wording changed.
- Verification (local files only): law.html parses with no unclosed tags; desktop `.nav-links` and `#mobile-menu` contain no Manufacturing / Local Businesses link; remaining `manufacturing.html` references in law.html are 2 (footer + body link-row) and `local-businesses.html` is 1 (footer). Live staging revalidation still required after push + Vercel rebuild — not yet done.

## FAQ: "What does the first step cost?" rewritten (2026-11-11, staging only)
- User request (with screenshot of the homepage FAQ): all initial audits and diagnostics are free and included with a free 30-minute initial conversation, where we go through what was found and, more importantly, find out where the exact problems are for the business owner. Their problem may not even be an audit — it may be something they are dealing with right now — and the audit is supplementary to that conversation, where the business's concerns get discussed.
- index.html only: the same answer did not appear verbatim on any other page in the assembly (grep confirmed), so no other page was changed.
- New answer, verbatim: "Nothing. The first audit or diagnostic is free, and it comes with a free 30-minute conversation. We go through what we found together, and more importantly, we find out where the exact problems are for your business. Your problem may not be an audit at all. It may be something you are dealing with right now, and the audit is there to support that conversation, not replace it. You keep the findings either way, and nothing commits you to paid work. For a manufacturer, that first step is Prime Diagnostics, and it starts with a conversation about your environment."
- FAQ question unchanged; no other FAQ answer, copy, facts, phone, email, fee, or timeline changed. No fee or timeline invented for the paid manufacturing step — it still only says Prime Diagnostics starts with a conversation about their environment. We voice kept throughout; "Prime Diagnostics" kept as the product name.
- Verification (local files only): index.html parses; new answer present verbatim; no old sentence remains in that FAQ. Live staging revalidation still required after push + Vercel rebuild — not yet done.

## FAQ wording tweak: "in the audit" (2026-11-11, staging only)
- User request: update it to "Your problem may not be in the audit at all"
- index.html only, FAQ "What does the first step cost?": changed "Your problem may not be an audit at all." to "Your problem may not be in the audit at all." Nothing else changed.
- Full answer now reads: "Nothing. The first audit or diagnostic is free, and it comes with a free 30-minute conversation. We go through what we found together, and more importantly, we find out where the exact problems are for your business. Your problem may not be in the audit at all. It may be something you are dealing with right now, and the audit is there to support that conversation, not replace it. You keep the findings either way, and nothing commits you to paid work. For a manufacturer, that first step is Prime Diagnostics, and it starts with a conversation about your environment."
- Verification (local files only): index.html parses; new sentence present once, old sentence zero times. Live staging revalidation still required after push + Vercel rebuild — not yet done.

## Industries dropdown: hover alone now keeps it open, no click needed (2026-11-11, staging only)
- User report (with screenshot of the old live deployment): the dropdown only stayed open if Industries was clicked; hovering showed it but it went away before an item could be selected. Asked for a researched fix, suggesting Stack Overflow.
- Research first (standard pattern, from the sources below): a hover dropdown closes when the pointer crosses a dead zone between trigger and panel. The fix is (1) the submenu must be a child of the hovered parent `li`, (2) hover is applied to the parent (`li:hover > ul`), never to the trigger anchor alone, (3) no gap between trigger and panel — bridge any visual gap with an invisible pseudo-element that spans the panel's width, or overlap the panel over the trigger, and (4) hide with a short delay / grace period instead of instantly. Sources: https://copyprogramming.com/howto/css-sub-menu-disappears-on-hover , https://copyprogramming.com/howto/drop-down-menus-won-t-stay-open , https://bespop.com/problems/mega-menu-submenu-closes-hover-gap.html
- Root cause found in index.html (local code, not the old live screenshot): the submenu IS a child of `li.nav-item` and `:hover` on the parent did open it, but the hover corridor was far too narrow. The panel is centred (`left: 50%; transform: translateX(-50%); min-width: 300px`) so it overhangs the ~150px trigger by ~70px a side, while the old bridge (`.nav-item::after`, 14px high, only 8px wider than the trigger on each side) covered almost none of that overhang. Any diagonal move down to a panel item left the `li` + bridge hover box before entering the panel, `:hover` dropped, and `display: none` shut the menu instantly. That is also why it only stayed open after a click: click adds `.is-open`, which holds it open regardless of hover. The earlier rendered-browser check confirmed the symptom: moving step-by-step vertically kept it open, moving directly/diagonally to a lower item closed it.
- Fix (index.html only):
  - `.submenu` no longer flips with `display: none/block`. It is always in the DOM but hidden with `opacity: 0; visibility: hidden; pointer-events: none`, and shown on `.nav-item:hover`, `:focus-within`, `.is-open`, and `.submenu:hover` with `opacity: 1; visibility: visible; pointer-events: auto`. Hiding uses `transition: opacity 160ms ease, visibility 0s linear 200ms`, i.e. a ~200ms grace period for a brief pointer excursion; showing has no delay.
  - `.submenu` now overlaps the trigger slightly (`top: calc(100% - 2px)`) so there is no 1px gap at the seam.
  - `.nav-item::after` bridge widened from 14px / trigger-width to 24px high and 340px wide, centred on the trigger — as wide as the panel — so the whole trigger-to-panel path is hoverable.
  - Added `.submenu::before` (24px high, full panel width, sitting just above the panel) as a second bridge from the panel's side, the same pattern manufacturing.html already uses for its Applications dropdown (`.nav-dropdown::before`).
  - Trigger highlight unchanged: hovering the label, the chevron, or anywhere in the submenu keeps the whole Industries pill highlighted (`.nav-item:hover > .nav-industries-control`, already in place). No click is required on desktop hover; touch/click behaviour unchanged (first tap opens via `.is-open`, second tap follows the link to #industries).
  - No copy, facts, phone, email, FAQ, or destinations changed. Desktop submenu still has the same 4 items: Industries overview, Services for Manufacturers, Services for Legal Professionals, Services for Local Businesses. Note: the user's screenshot showed a 5th item, "Manufacturing Industries", but that is the old live deployment; the current staging submenu deliberately has 4 (the duplicate Manufacturing Industries entry was removed in an earlier UAT fix; it is still linked from the footer). It was NOT re-added.
  - Other pages NOT touched: none of them has an Industries dropdown. manufacturing.html has an Applications dropdown (already uses the opacity/visibility + bridge pattern), manufacturing-industries.html has an Applications dropdown that is click-only (different structure, out of scope), law.html and local-businesses.html have no dropdown in the top nav.
- Verification (local files only): index.html parses with no unclosed tags (HTMLParser check, zero errors); inline script passes `node --check`; submenu confirmed a child of `li#industries-item`; no `display: none` remains on `.submenu`; new bridge / grace-period rules present; all 4 submenu destinations unchanged. No headless browser is installed in this VM (no Chromium/Firefox/Playwright), so no rendered hover probe could be run here — that is stated plainly, not assumed. Live staging revalidation still required after push + Vercel rebuild, on the CURRENT deployment URL, not the frozen preview URL — not yet done.
