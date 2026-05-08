# Prime AI Consultants — Marketing Site

Static marketing site implementing the v6 design from Claude Design.

## Local preview

Open `index.html` directly in any modern browser, or run a tiny local server:

```bash
# Option A — Python
python3 -m http.server 8000

# Option B — Node
npx serve .
```

Then visit http://localhost:8000.

## Deploy to Vercel

This site is plain static HTML/CSS — no build step required.

### Option 1 — Vercel CLI (fastest)

```bash
npm install -g vercel
cd "Prime AI Consultants"
vercel
```

Follow the prompts. For production:

```bash
vercel --prod
```

### Option 2 — Git + Vercel Dashboard

1. Push this folder to a GitHub repo (e.g. `prime-ai-consultants`).
2. Go to https://vercel.com/new and import the repo.
3. Framework preset: **Other** (or "No framework detected").
4. Build command: leave **empty**.
5. Output directory: **`.`** (the project root).
6. Click **Deploy**.

`vercel.json` is already configured with sensible cache headers and security defaults.

### Custom domain

After deploying, in the Vercel dashboard go to **Settings → Domains** and add your domain (e.g. `primeai-consultants.com`). Vercel will give you DNS records to point at.

## Files

```
.
├── index.html          # The site
├── assets/
│   ├── styles.css      # All styling
│   └── favicon.svg     # Bloom Tech mark
├── vercel.json         # Deploy config
└── README.md           # This file
```

## Brand tokens

| Token | Value | Use |
|---|---|---|
| Blue | `#0052CC` | Primary brand |
| Purple | `#6366F1` | Accent, italic emphasis |
| Navy | `#0B1437` | Dark sections, body ink |
| Cream | `#F4EFE6` | Hero / CTA background |
| Lilac | `#F2EBFE` | "Why Choose Us" surface |

Type: **Inter** (UI) + **Cormorant Garamond** (italic accents).
