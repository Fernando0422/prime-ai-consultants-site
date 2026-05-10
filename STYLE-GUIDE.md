# Prime AI Consultants — Visual style guide

**Canonical reference:** the **Methodology** page (`methodology.html` + `body.page-methodology` rules in `assets/styles.css`). Use this doc when aligning other routes so typography, spacing, color usage, and components stay predictable.

Implementation note: **`body.page-home`** (homepage), **`body.page-route`** (AI for MES / ERP / CRM, Services, Company, Contact), and **`body.page-methodology`** share the methodology rail: **`32px` section eyebrows**, **flat navy `page-hero`**, **`h-h1` + `lede` on dark heroes**, dual-CTA panel density, and (where relevant) **`#5a5a7e` prose**. Legal pages omit `page-route` so heroes keep the default texture treatment.

---

## 1. Brand tokens (`:root`)

Defined in **`assets/styles.css`**. Prefer tokens over raw hex.

| Role | Token / value | Notes |
|------|-----------------|-------|
| Page / plate dark | `#0A0F1E` (`--color-dark`) | Hero, navy outcome strips, dual CTA dark panel |
| Body text | `#1A1A2E` (`--color-text-dark`), secondary **`#5a5a7e`** where used on methodology |
| Accent (UI chrome, borders, dark BG) | `--color-teal` `#00D4B8` | Focus rings, left accents, eyebrows on dark |
| **Readable teal on light** | `--color-teal-text-on-light` `#0d7d72` | **Required** for small teal text on `#FFFFFF` or `--color-mist` (brand teal fails WCAG) |
| Structural blue | `#0a4a7e` | Phase numbers labels, bullets, list markers in light accordion |
| Surfaces | `--color-mist`, `--color-off-white`, `--color-white`, `--color-border` | Section backgrounds |

**Rule:** `#00D4B8` is for **emphasis on dark backgrounds** or large UI geometry—not for dense body copy on white.

---

## 2. Typography

**Families:** **Manrope** (UI + headings via `--font-display` / `--font-body`), **Fraunces** as **`--font-serif-accent`** on horizon phase labels (“Now”, “Next”, “Scale”). JetBrains Mono for monospace labels (`--font-mono`). Loaded via the `@import` at the top of **`assets/styles.css`**.

### 2.1 Section eyebrows (canonical methodology scale)

Eyebrows use `.eyebrow` (uppercase, bold, teal; bracket décor from base utility unless overridden).

| **Dark `page-hero` eyebrow** | **`32px`**, **`letter-spacing: 0.12em`** (`assets/styles.css` → `.page-hero .eyebrow`, `.page-home .hero .eyebrow`) |
| **Interior section rails** (methodology phases, homepage `main`, **route** marketing pages) | Same scale via **`main .section-head .eyebrow`** under **`page-methodology` / `page-home` / `page-route`** (+ homepage stats bar) |

Selectors (see `styles.css` for the live list):

```css
.page-hero .eyebrow,
.page-home .hero .eyebrow { /* 32px / 0.12em — all dark page heroes */ }

.page-methodology .phase-overview .section-head .eyebrow,
.page-methodology .phases-section .section-head .eyebrow,
.page-home main .section-head .eyebrow,
.page-home .stats-bar .eyebrow,
.page-route main .section-head .eyebrow { /* interior rails */ }
```

**`body.page-route`:** add to **`ai-mes.html`**, **`ai-erp.html`**, **`ai-crm.html`**, **`services.html`**, **`company.html`**, **`contact.html`** for shared rails without duplicating selectors per file.

Dark hero copy is standardized in CSS (no inline color needed):

```css
.page-hero .h-h1 { color: #fff; max-width: 920px; }
.page-hero .lede { margin-top: 24px; color: rgba(255,255,255,0.78); }
.page-hero .cta-row { margin-top: 36px; }
```

### 2.2 Headlines

Use existing utilities **`h-h1`**, **`h-h2`**, **`lede`** for page title, section title, and supporting line. Clamp sizes come from `--text-h1`, `--text-h2`, etc. in `:root`.

### 2.3 Methodology roadmap (light strip)

| Element | Treatment |
|---------|-----------|
| Strip title (“MES + AI Integration Roadmap”) | **16px**, **700**, uppercase, teal **on light** uses `--color-teal-text-on-light` via scoped rules |
| “Cross-cutting foundations…” kicker | **16px**, **700**, uppercase, muted gray-brown |
| Phase card week row | **`--color-teal-text-on-light`** at **13px**, **600** |

### 2.4 Highlight / outcome navy plate (`.outcome-milestone`)

| Element | Class | Treatment |
|---------|-------|-------------|
| Small label | `.outcome-milestone-eyebrow` | **20px**, **600**, teal, uppercase, short bar ornament |
| Lead line | `.outcome-milestone-lead` (+ `strong`) | White, clamp ~17–20px |
| Detail | `.outcome-milestone-detail` | Off-white tint, clamp ~16–18px |
| Closing | `.outcome-milestone-tail` | White, semi-bold clamp ~15–17px |

Plate: background **`#0a0f1e`**, **4px** left teal bar, **`border-radius: 8px`**, centered inner (`outcome-milestone-inner` **`max-width: min(58rem, 100%)`**).

Roadmap-contained outcome **must** keep `.roadmap-native-outcome.outcome-milestone` so it wins over the faint mint roadmap outcome tint (accessibility).

### 2.5 Accordion phases (reference implementation)

Applicable to **`.phase-detail-list--accordion`** on methodology (`body.page-methodology`):

| Piece | Font size |
|-------|-----------|
| Trigger: phase index + title | **20px**, **600** |
| Timeline pill (“Week…” / “Weeks…”) | **14px**, **600**, uppercase-ish spacing **0.06em** |
| Expand control (`+`) | **20px** in **34×34** touch box |
| Column labels (“What we do”, …) | **18px**, letter-spacing **0.08em** |
| Paragraphs & list rows | **16px** |

### 2.6 Dual CTA rails

Methodology + homepage + **`page-route`** marketing pages: **`.dual-cta { gap: 0 }`** so panels touch; panels **`font-size: 20px`**, **`font-weight: 600`**; light panel **`#f2f2f5`**; dark hover **`#141d33`**.

---

## 3. Layout & rhythm

| Concept | Guidance |
|---------|----------|
| Content width | `.container` — **`max-width: 1240px`**, horizontal **`--content-pad-x`** |
| Default section padding | **`--section-pad`** / **`section-pad-sm`** on `.section` |
| Phase overview (methodology) | Extra bottom ease: **`padding-bottom: clamp(40px, 6vw, 72px)`** on `.phase-overview.section` |
| Phase detail stack (methodology) | Tighter top: **`padding-top: clamp(24px, 4vw, 48px)`** on `.phases-section.section` |

---

## 4. Motion

| Pattern | Behavior |
|---------|----------|
| In-view entrance | `.reveal` + JS `IntersectionObserver` in **`assets/site.js`** — fade + **`translateY(var(--reveal-distance))`**, ~**0.78s** `cubic-bezier(0.22, 1, 0.36, 1)` |
| Reduced motion | `prefers-reduced-motion`: reveal content **no animation**, visible immediately |
| Anchor jumps | **`scroll-behavior: smooth`** disabled when user prefers reduced motion |

Add **`class="reveal"`** to discrete blocks you want staggered while scrolling—not to every sibling.

---

## 5. Accessibility checklist (methodology-tested)

1. Eyebrows and small labels on **white/mist**: use **`--color-teal-text-on-light`**, not raw **`--color-teal`**.
2. Outcome stripes on roadmap: navy **`.outcome-milestone`**, never the default light teal wash as the sole background behind near-white copy.
3. Focus: visible **teal outline** on interactive controls (globally scoped `focus-visible` rules).

---

## 6. Rolling out to other pages — practical order

1. **Body / layout:** same **nav**, **announce**, **`main`**, **footer** shell as methodology.
2. **Hero:** `page-hero` + `.eyebrow` at **section eyebrow scale (32px)** once you replicate the methodology selector or introduce a shared class (e.g. `.eyebrow--section-xl`).
3. **Sections:** `section` + background tokens (`section-light`, `-mist`, `-off-white`, `section-dark`).
4. **Section heads:** `section-head` with `.eyebrow` + **`h-h2`** + optional **`lede`**.
5. **Motion:** sprinkle **`reveal`** on major folds (matching methodology density—don’t overuse).
6. **Closing CTAs:** `dual-cta-section` > `dual-cta` grid, **`gap: 0`** for edge-to-edge pair.
7. **CSS cleanup (later):** move repeated `.page-methodology …` bundles to **modifiers** (`--density`, `--eyebrow-xl`) once all pages share the same HTML shape.

---

## 7. File map

| File | Responsibility |
|------|----------------|
| **`assets/styles.css`** | Tokens, components, methodology scope, reveal |
| **`assets/site.js`** | Reveal observer, accordion behavior, anchors |
| **`methodology.html`** | Reference markup for hero → intro → phased content → milestone → dual CTA |

---

## 8. Changelog cue

When you ship site-wide alignment, note in **`CHANGELOG`** (if you maintain one): which pages adopted section eyebrow scale, accordion type scale, outcome pattern, dual-CTA gutter, and readable-teal audits.
