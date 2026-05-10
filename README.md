# Prime AI Consultants — Marketing Site

Static marketing site for Prime AI Consultants. Plain HTML / CSS / JS — no build step.

## Pages

| Path | Purpose |
|---|---|
| `index.html` | Homepage (12 widgets: hero, stats, problem, services, methodology preview, proof, differentiators, team, dual CTA) |
| `methodology.html` | Full 10-phase MES + AI integration framework |
| `services.html` | Three engagements (Diagnostics, Build, Retainer) + system pages |
| `ai-mes.html` | AI for MES (manufacturing) |
| `ai-erp.html` | AI for ERP (SAP, Oracle, NetSuite, Dynamics) |
| `ai-crm.html` | AI for CRM (Salesforce, HubSpot, Dynamics) |
| `company.html` | About / mission / principles / team |
| `contact.html` | Contact form + discovery call info |
| `privacy.html` | Privacy Policy (starter — replace with Termly output) |
| `terms.html` | Terms of Service (starter — replace with Termly output) |

## Required setup before going live

### 1. Wire the contact form to Formspree (5 minutes)

The contact form posts to a placeholder Formspree endpoint. To activate it:

1. Sign up at [formspree.io](https://formspree.io) (free tier: 50 submissions/month).
2. Create a new form. Set the destination email to `hello@primeaiconsultants.com`.
3. Copy your form ID (looks like `xrgvabcd`).
4. In `contact.html`, find this line:

   ```html
   action="https://formspree.io/f/YOUR_FORM_ID"
   ```

   and replace `YOUR_FORM_ID` with your actual ID.

5. Test by submitting the form. The first submission requires email confirmation.

If `YOUR_FORM_ID` is left in place, the form shows an inline error directing visitors to email `hello@primeaiconsultants.com` directly — so the site never silently drops a lead.

### 2. Methodology roadmap (native widget)

The 10-phase MES + AI integration roadmap is rendered as semantic HTML/CSS (see `.roadmap-native` and related classes in `assets/styles.css`) on both `index.html` and `methodology.html`: horizontal-scroll phase cards, cross-cutting foundations, and an outcome block. Update copy by editing the markup in those files; no PNG is required live.

Legacy file `assets/MES___AI_Integration_roadmap_-_Phase_Diagram.png`, if present, is optional reference only.

### 3. Replace legal pages with Termly output (recommended)

`privacy.html` and `terms.html` ship with reasonable starter content, but you should generate finalized versions through [Termly](https://termly.io) or [Iubenda](https://www.iubenda.com) and replace the body content. The page chrome (nav, footer, styling) stays the same.

### 4. Logos

Primary navigation loads `assets/prime-ai-logo-dark-bg.svg` with height `48px` and auto width (`assets/styles.css` `.brand-logo`). `prime-ai-logo-light-bg.svg` ships in `/assets/` for light backgrounds (deck templates, alternate headers).

### 5. (Optional) Alternate hero visuals

Homepage `.hero-bg` defaults to a dark gradient mesh (no raster image). Alternate treatments live in `.hero-wafer-bg` and `.hero-grid-bg` in `assets/styles.css`; wire the class onto the `.hero-bg` element if you drop in photography later.

## Local preview

```bash
# Option A — Python
python3 -m http.server 8000

# Option B — Node
npx serve .
```

Then visit http://localhost:8000.

## Deploy to Vercel

```bash
npm install -g vercel
cd "Prime AI Consultants"
vercel        # preview deploy
vercel --prod # production
```

Or push to GitHub → import on [vercel.com/new](https://vercel.com/new) → Framework preset: **Other** → Build: **(empty)** → Output: **`.`** → Deploy.

`vercel.json` includes:
- Clean URLs (`/methodology` instead of `/methodology.html`)
- Permanent redirects from removed pages (`/ai-individuals`, `/levels-of-ai`)
- Long-lived cache headers for `/assets/*`
- Standard security headers (`X-Frame-Options`, `Referrer-Policy`, etc.)

## Brand & design tokens

Defined as CSS custom properties at the top of `assets/styles.css`.

| Token | Value | Use |
|---|---|---|
| `--color-dark` | `#0A0F1E` | Primary dark sections (Palantir-style backdrop) |
| `--color-teal` | `#00D4B8` | Primary accent — eyebrows, CTAs, hover states |
| `--color-teal-dark` | `#00A896` | Hover for primary buttons |
| `--color-off-white` | `#F8F8F6` | Service-card section background |
| `--color-mist` | `#F5F5F7` | Stats bar / subtle section dividers |
| `--color-text-dark` | `#1A1A2E` | Body text on light backgrounds |
| `--color-text-body` | `#4A4A5A` | Secondary body / paragraph text |

Typography:
- **Inter Tight** for display headlines
- **Inter** for body and UI copy
- **JetBrains Mono** for eyebrow labels, stats, and roadmap chips

Loaded from Google Fonts.

## File map

```
.
├── index.html          # Homepage
├── methodology.html    # 10-phase framework
├── services.html       # 3 engagements + system pages
├── ai-mes.html         # AI for MES
├── ai-erp.html         # AI for ERP
├── ai-crm.html         # AI for CRM
├── company.html        # About / team
├── contact.html        # Contact form (Formspree)
├── privacy.html        # Privacy Policy stub
├── terms.html          # Terms of Service stub
├── assets/
│   ├── styles.css      # Full design system
│   ├── site.js         # Nav, mobile, form, sticky CTA, reveal
│   ├── favicon.svg
│   ├── prime-ai-logo-dark-bg.svg  # Navbar logo (preferred on dark chrome)
│   ├── prime-ai-logo-light-bg.svg  # For light backgrounds (optional)
│   ├── founder-antonio.png
│   ├── founder-fernando.png
│   ├── MES___AI_Integration_roadmap_-_Phase_Diagram.png  # Optional reference only
│   ├── hero-manufacturing.jpg      # Unused by default (.hero-bg is gradient-only)
│   └── hero-wafer.jpg               # Alternate hero preset via .hero-wafer-bg
├── page_content/       # Legacy fragment templates (unused — kept for reference)
├── scripts/            # Legacy Python content generators (unused — kept for reference)
├── vercel.json         # Deploy config + redirects
└── README.md
```

The `page_content/` and `scripts/` folders are from a previous build pipeline and are no longer wired into the site. They can be deleted if you want a leaner repo.
