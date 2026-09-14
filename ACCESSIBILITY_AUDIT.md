# Accessibility & Code-Correctness Audit — prime-ai-consultants-site

**Date:** 2026-09-14
**Scope:** all 13 deployed pages
**Standard:** WCAG 2.2 Level AA
**Method:** headless Chrome driven over the DevTools Protocol. Chrome's own accessibility tree for
accessible names, real rendered-pixel sampling for contrast, real dispatched key events for keyboard
operability, and pixel diffs to confirm visual state changes. No source code was modified.

---

## Headline

**The site has no WCAG A or AA failures that I could reproduce. One low-severity ARIA pattern defect.**

Every page passes the structural and interaction fundamentals, and **all three findings from my first
pass turned out to be false positives**, each disproved by stronger evidence. That correction is the
most important part of this report, so it is documented in full below rather than quietly dropped.

---

## Verified passing

| Check | Result | Evidence |
|---|---|---|
| `lang` attribute on `<html>` | PASS, 13/13 | `lang="en"` |
| Exactly one `<h1>` per page | PASS, 13/13 | 1 on every page |
| Skip link to main content | PASS, 13/13 | first tab stop; activates and moves focus |
| Landmarks | PASS, 13/13 | `nav`, `main`, `footer[contentinfo]`; `aside` where used |
| Single `<main>` | PASS | no duplicates |
| Form fields labelled | PASS | contact.html: 7 fields, 0 unlabelled |
| Images have `alt` | PASS | 0 missing `alt` across 13 pages |
| `alt` quality | PASS | descriptive, includes founders' titles |
| Accessible names on interactive elements | **PASS: 0 unnamed** | Chrome AX tree, 13/13 pages |
| Duplicate `id` attributes | PASS | none |
| Broken ARIA references | PASS | `aria-labelledby` / `describedby` / `controls` all resolve |
| Positive `tabindex` | PASS | none; tab order follows DOM |
| `onclick` on non-interactive elements | PASS | none |
| Viewport allows zoom | PASS | no `user-scalable=no`, no `maximum-scale=1` |
| Meta description | PASS | present on 13/13 |
| `target="_blank"` | PASS | all carry `rel="noopener noreferrer"` |
| JS console errors | **PASS: 0** | no errors or exceptions on any page |
| Touch targets | PASS | no interactive target under 24x16 CSS px |
| Focus indicator visible | PASS | 17.53% pixel change when focused (see F1) |
| Dropdown keyboard operable | PASS | focus opens, Tab traverses all 4 links (see F2) |

### Color contrast — measured from real rendered pixels

| Region | Real ratio | Required | Result |
|---|---|---|---|
| Footer disclaimer (14px) | 4.93 | 4.5 | PASS |
| Methodology lane title (12.5px bold) | 5.83 | 4.5 | PASS |
| Footer column heading (12.5px bold) | 6.70 | 4.5 | PASS |
| Footer tagline (16px) | 6.88 | 4.5 | PASS |
| Footer legal links (14px) | 7.18 | 4.5 | PASS |
| Methodology lane note (14.7px) | 7.52 | 4.5 | PASS |

---

## Finding: F1 — LOW: Escape does not close the Services dropdown

**WAI-ARIA Authoring Practices (disclosure navigation pattern). Not a WCAG A/AA failure.**

The desktop Services dropdown opens on focus and hover, is fully traversable by keyboard, and sets
`aria-expanded` correctly. One behavior deviates from the expected pattern:

```
A. trigger focused            : display=block expanded=true  links=4  active="Services"
B. focus inside submenu       : display=block expanded=true  links=4  active="AI for MES"
C. immediately after Escape   : display=block expanded=true  links=4  active="Services"
D. 600ms after Escape         : display=block expanded=true  links=4  active="Services"
```

**What happens:** pressing Escape moves focus back to the trigger, but the menu stays open and
`aria-expanded` remains `true`.

**Why:** `site.js:100-108` handles Escape by calling `setOpen(false)` then `trigger.focus()`. The
focus triggers the `focusin` listener at `site.js:92-94`, which calls `setOpen(true)` again. The
close is immediately undone by the refocus.

**Impact:** minor. A keyboard user cannot dismiss the menu with Escape. They can still move away with
Tab (the `focusout` handler closes it), and the menu does not trap focus. No content is unreachable.

**Suggested fix:** suppress the `focusin` re-open immediately after an Escape-triggered refocus, for
example with a short-lived flag or by checking a "just escaped" state before calling `setOpen(true)`.

---

## Corrected false positives

All three items below were reported as defects by my first automated pass. Each is **not** a real
defect, and each was disproved by a different measurement technique. Recording them because a
single-pass tool would have reported the same things and they would have been wrong.

### 1. "13 links with no accessible name" — NOT A DEFECT

**What my check did:** compared `a.textContent.trim()` against an empty string.

**Why it was wrong:** `textContent` ignores the text alternative of a contained image. The footer
logo link contains `<img alt="Prime AI Consultants">`, so it has a valid accessible name computed
from content, which `textContent` does not expose.

**Ground truth:** Chrome's accessibility tree (`Accessibility.getFullAXTree`) reports **0 interactive
elements without a name** across all 13 pages, including all links, buttons, and form controls.

### 2. "6 to 8 contrast failures per page, worst 1.03:1" — NOT A DEFECT

**What my check did:** compared computed `color` against computed `backgroundColor`, walking ancestors
for the first non-transparent background.

**Why it was wrong:** it did not composite alpha. Footer text is `rgba(232, 236, 242, 0.58)` over a
dark panel. My check effectively compared that near-white against white, producing a nonsense
1.03:1.

**Ground truth:** sampling the actual rendered pixels of each region gives 4.93:1 to 7.52:1, all
passing AA. Measuring the rendered PNG removes alpha, blending, and gradient questions entirely.

### 3. "In-body anchor links have no focus indicator" — NOT A DEFECT

**What my check did:** captured a clipped screenshot with `captureBeyondViewport: true` before and
after focusing, then diffed pixels. It reported 0 changed pixels.

**Why it was wrong:** two compounding errors.
- The first test targeted the submenu's duplicate links, which have zero size while the panel is
  `display: none`. Focusing a zero-size element cannot paint anything.
- `captureBeyondViewport: true` does not paint focus rings. Elements outside the viewport rendered
  identically whether focused or not, which is why the diff was exactly 0.

**Ground truth:** with the link inside the actual viewport, the focus ring paints and the diff is
unambiguous:

| Measurement | Changed pixels | % changed | Max channel delta |
|---|---|---|---|
| In-viewport link | 2,760 / 15,744 | **17.53%** | 384 |

Computed style confirms `outline: solid 3px rgb(59, 168, 154)` with `outline-offset: 3px`.

### 4. "Services dropdown is hover-only and not keyboard-operable" — NOT A DEFECT

**What my earlier check did:** focused the trigger, pressed Enter, observed no change in
`aria-expanded`, and concluded the menu could not be opened.

**Why it was wrong:** the trigger is an `<a href="services.html">`. Pressing Enter **navigated to
services.html**, so I was reading the state of a freshly loaded page, not the effect of Enter on the
menu. I also read `aria-expanded` from the wrong element, because the footer contains a second
element matching the same selector.

**Ground truth** (1400px viewport, real focus and key events):

```
initial (nothing focused)  : display=none  expanded=false  links visible 0/4
trigger FOCUSED            : display=block expanded=true   links visible 4/4
Tab 1                      : "Services overview"  in submenu, visible
Tab 2                      : "AI for MES"         in submenu, visible
Tab 3                      : "AI for ERP"         in submenu, visible
```

The dropdown opens on focus, exposes `aria-haspopup="true"` and `aria-controls="nav-sub-services"`,
toggles `aria-expanded`, and every submenu link is reachable and visible by keyboard. This is correct
and, in fact, better than most implementations.

**Lesson applied:** for interactive verification, always assert on the same element and the same
document instance, and never infer "nothing happened" from a state read after a possible navigation.

---

## Page-by-page structure

| Page | h1 | Landmarks | Skip link | Meta desc | Console errors |
|---|---|---|---|---|---|
| index.html | 1 | nav, main, footer | yes | yes | 0 |
| diagnostics.html | 1 | nav, main, footer | yes | yes | 0 |
| methodology.html | 1 | nav, main, aside, footer | yes | yes | 0 |
| services.html | 1 | nav, main, footer | yes | yes | 0 |
| ai-mes.html | 1 | nav, main, footer | yes | yes | 0 |
| ai-erp.html | 1 | nav, main, footer | yes | yes | 0 |
| ai-crm.html | 1 | nav, main, footer | yes | yes | 0 |
| company.html | 1 | nav, main, footer | yes | yes | 0 |
| contact.html | 1 | nav, main, aside, footer | yes | yes | 0 |
| privacy.html | 1 | nav, main, footer | yes | yes | 0 |
| terms.html | 1 | nav, main, footer | yes | yes | 0 |
| accessibility.html | 1 | nav, main, footer | yes | yes | 0 |
| 404.html | 1 | nav, main, footer | yes | yes | 0 |

---

## Health score

| Category | Weight | Score | Basis |
|---|---|---|---|
| Console | 15% | 100 | 0 errors across 13 pages |
| Links | 10% | 100 | no broken links found |
| Visual | 10% | 100 | no visual defects found |
| Functional | 20% | 98 | Escape does not close the dropdown |
| UX | 15% | 98 | same |
| Content | 5% | 100 | headings and labels coherent |
| Accessibility | 15% | 98 | no A/AA failures; one ARIA pattern deviation |

Weighted: 99.0 points over 0.90 total weight (Performance excluded, not measured).

**Weighted score: 99 / 100**

*Performance was not measured. Core Web Vitals, LCP, and bundle size need a separate
Lighthouse-style run with network throttling. Excluded from the total rather than estimated.*

---

## Recommended next steps

1. **F1** — fix the Escape re-open interaction in `site.js`. Small, contained change.
2. **Optional** — add `axe-core` or `pa11y` to CI. The site would pass today; the value is catching
   future regressions.
3. **Not covered by this audit** — performance, and testing with real assistive technology
   (NVDA, JAWS, VoiceOver). No automated method substitutes for either.

---

## Method notes

Techniques that produced trustworthy results, and the traps avoided:

- **Accessible names:** use the browser's accessibility tree, never string matching on `textContent`.
- **Contrast:** sample rendered pixels; never compare computed `color` values without compositing.
- **Focus visibility:** the element must be inside the viewport, and `captureBeyondViewport: true`
  must not be used, or focus rings will not paint.
- **Keyboard behavior:** dispatch real key events and re-read state on the same document. A link
  trigger navigates on Enter, which invalidates any post-press state read.
- **Element targeting:** the footer duplicates nav link text. Scope selectors to the nav container.
