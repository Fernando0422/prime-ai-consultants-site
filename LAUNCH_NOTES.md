# Launch verification checklist

Updated 2026-07-29. Copy baseline: v2.0 (legally conservative). Status values: **Done** · **Verified in code** · **Needs you** · **Needs counsel**.

This is an operational checklist, not legal approval. Terms and Privacy remain marketing-legal drafts until counsel reviews them.

Push history: see [UPDATE_REPORTS/2026-07-29-push.md](UPDATE_REPORTS/2026-07-29-push.md).

## Confirmed site configuration

| Item | Value | Status |
| --- | --- | --- |
| Business email | `hello@primeaiconsultants.com` | Verified in code |
| Privacy / Terms contact email | `hello@primeaiconsultants.com` | Verified in code |
| Form processor | Formspree form id `xgoqorke` (`assets/site.js`, `contact.html`) | Verified in code |
| Hosting | Vercel | Verified in code |
| Analytics product | None (no GA / pixels) | Verified in code |
| Scheduling provider | Removed | Done |
| Legal effective date | July 16, 2026 | Verified in code |
| Fernando LinkedIn | `https://www.linkedin.com/in/fernando-rojas0422/` | Done |
| Antonio LinkedIn | `https://www.linkedin.com/in/antonio-rojas-31016022/` | Done |
| Canonical host in HTML | `https://www.primeaiconsultants.com` | Verified in code (confirm DNS/production) |

## Human / launch items

| # | Item | Status | Notes |
| --- | --- | --- | --- |
| 1 | Live Formspree smoke test | Done (API) / Needs you (inbox) | One POST to `https://formspree.io/f/xgoqorke` on 2026-07-29 returned HTTP **200** with `{"ok":true,"next":"/thanks"}`. Payload labeled "Prime AI Launch Test" / message "LAUNCH TEST. Please ignore…". **Check Formspree dashboard + `hello@` inbox** and delete the test submission. Success UI path is wired in `assets/site.js` (`res.ok` → `#form-success`). |
| 2 | Fernando LinkedIn URL | Done | Set in `assets/site.js`, footer partial, `index.html`, `company.html`, `contact.html`. |
| 3 | Antonio LinkedIn URL | Done | Same as above. |
| 4 | Announcement bar (LA summer) | Done | No `#announce-bar` / `.announce` markup on live HTML pages. CSS/JS still support it if re-added. Privacy wording softened accordingly. |
| 5 | Canonical / production hostname | Needs you | Confirm production serves `www.primeaiconsultants.com` (and redirects) matching page canonicals. |
| 6 | Mailing address on Privacy / Terms | Needs you + Needs counsel | Placeholder `[MAILING ADDRESS TBD]` on Privacy §15 and Terms §13. Do not invent a home or private address. Contact page currently shows marketing location "Based in Los Angeles, California" (not a street address). |
| 7 | Public phone on Contact | Needs you | Contact aside shows `(805) 216-4651`. Confirm this is the intended public number and owner. |
| 8 | LA / CA governing-law fit | Needs you + Needs counsel | Marketing location Los Angeles, California (Phoenix base removed as incorrect). Terms governing law California; venue county TBD (`[VENUE COUNTY TBD]`). |
| 9 | Legal entity name | Needs counsel | Pages use **Prime AI Consultants LLC**. Confirm formation, exact legal name, and registration state before treating as final. |
| 10 | Antonio biographical claims | Needs you | See quote below. Obtain Antonio's written OK before public launch. |
| 11 | Fernando bio / credentials | Needs you | Confirm SCU / Harvard Extension wording still accurate. |
| 12 | Counsel review of Terms / Privacy | Needs counsel | See counsel checklist below. Not attorney-approved. |

### Antonio bio currently on site (needs confirmation)

From `company.html`:

> Antonio's been in enterprise applications and IT for more than three decades. Since 2007, his publicly stated role has included senior applications development leadership in semiconductor manufacturing, including SAP applications development and LATAM project leadership.
>
> Publicly stated experience covers SAP, Infor (Mapics), Oracle, ERP implementations across the United States and Mexico, systems integration, and cross-border work. …

**Recommended action:** Antonio reviews `company.html` and homepage founder blurb; confirm or edit years, titles, systems, and geography. Do not invent replacements.

### Fernando bio currently on site (needs confirmation)

From `company.html`:

> … B.S. in Web Design and Engineering from Santa Clara University and is pursuing a Master of Liberal Arts in Computer Science at Harvard Extension School.

**Recommended action:** Confirm degree wording and current enrollment status.

## Removed intentionally (still true)

- Ai4 toast / Las Vegas event marketing
- Unsupported metrics, testimonials, case studies, platform logo walls
- Guaranteed timelines and “you own everything” language
- “The next AI revolution is in the physical world” footer statement
- Missing hero video placeholders (diagram labels used instead)

---

## Counsel review checklist

**Not legal advice.** Send counsel the documents and questions below. Do not treat website publication as counsel-approved until an attorney says so.

### What the site does (data flows)

1. **Static marketing site** hosted on **Vercel** (HTML/CSS/JS; no app login, no customer portal).
2. **Contact form** (`contact.html`) posts to **Formspree** (`https://formspree.io/f/xgoqorke`). Fields: name, email, company, role, primarySystem, message, timeline, optional interest. Client JS in `assets/site.js` uses `fetch` + `Accept: application/json`.
3. Formspree typically **emails submissions** to the configured inbox (expected: `hello@primeaiconsultants.com`). Confirm destination in Formspree dashboard.
4. **No separate analytics product** embedded. Vercel may still produce access/server logs.
5. **Google Fonts** loaded from Google; may receive IP / request metadata on page load.
6. Optional **localStorage** for announcement dismissal if an announce bar is present (currently not in HTML).
7. Public contact channels: email, phone `(805) 216-4651`, LinkedIn profile links, marketing location Los Angeles, California.
8. No payment processing, no account signup, no cookies banner (no advertising cookies claimed).

### Documents / paths to send counsel

| Document | Path / URL |
| --- | --- |
| Terms of Use | `terms.html` → `/terms` |
| Privacy Policy | `privacy.html` → `/privacy` |
| Accessibility statement | `accessibility.html` |
| Contact form + notices | `contact.html` |
| This checklist | `LAUNCH_NOTES.md` |
| Formspree terms / DPA | formspree.io account + vendor DPA |
| Vercel data processing docs | vercel.com account / DPA |
| Entity formation docs | [TBD: supply counsel] |

### Open questions for counsel

1. Is **Prime AI Consultants LLC** the correct contracting and website operator name? Formation state? Any DBA?
2. What **mailing / registered address** should appear on Privacy and Terms (if any)?
3. Is **California** governing law and California venue appropriate given Los Angeles, California marketing location? Which **county / district**?
4. Are limitation-of-liability and indemnity clauses in Terms sections 9 and 10 appropriate for a public marketing site? Caps? Carve-outs?
5. Does Formspree require a signed **DPA** / subprocessor review for this use case?
6. **CCPA / CPRA** applicability (revenue, volume, sale/share definitions)? Current Privacy §10 is carefully non-claiming.
7. **GDPR / UK GDPR** applicability for EU/UK visitors? Any need for an international-transfer / lawful-basis section?
8. Is naming **Google Fonts** / CDN IP processing sufficient, or should fonts be self-hosted?
9. Any required **cookie / preference** notice given current stack?
10. Phone number publication and SMS/call recording rules (if any)?
11. Bio / professional-experience claims: any advertising or employer-confidentiality risk beyond existing scope notices?

### Items already strengthened in-copy (2026-07-29)

- Privacy aligned to actual form fields; notes form does not collect phone.
- Privacy explicitly describes **Formspree** submission flow and **Vercel** hosting.
- Privacy notes **Google Fonts** / CDN technical request data.
- Privacy disclosure list names Formspree, Vercel, email providers.
- Privacy security clause notes third-party transmission limits (no overclaim).
- Terms intro names **Prime AI Consultants LLC** and scopes Terms to the marketing site.
- Terms / Privacy contact blocks use `[MAILING ADDRESS TBD]` placeholder.
- Terms venue notice uses `[VENUE COUNTY TBD]`; marketing base is Los Angeles, California (Phoenix marketing location removed as incorrect).
- Existing scope notices retained on liability, indemnity, CCPA non-claim, and founder employer disclaimers.
