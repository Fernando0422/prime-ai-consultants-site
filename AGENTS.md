# Prime AI Consultants — Website Project Context

**Generated:** August 17, 2026, from the Prime AI Consultants project (built collaboratively in Claude/Cowork).
**Scope note:** This is the **site-scoped** version of the Prime AI Consultants handoff, meant to live inside `~/prime-ai-consultants-site` (the deployed website repo). It intentionally excludes internal business systems (Supabase control plane, CRM/relationship pipeline, agent roster) that have no business being inside a deployed codebase's git history. The full version, including that internal-systems section, lives separately in `~/prime-ai-consultants-ops` — reference it directly for anything beyond brand, copy, and site UX.
**Purpose:** Give any AI coding/writing agent — including DeepSeek Harness — full context on Prime AI Consultants brand, voice, and website so work can continue without re-deriving decisions already made. DeepSeek Harness (and most agent CLIs) read a root-level `AGENTS.md` automatically as standing context.

If you are an AI agent reading this: treat everything below as settled fact and established decisions, not suggestions to re-litigate. Ask the user before deviating from anything marked as a rule (banned words, colors, pricing, etc.).

---

## 1. Company Snapshot

**One-sentence position:** Prime AI Consultants builds the AI intelligence layer that manufacturers can trust, because the methodology was built inside a real semiconductor fab before it was sold to anyone.

**Founders:**
- **Antonio Rojas** — 18 years inside Semtech's semiconductor manufacturing operations. Built and validated the methodology in production: a 400-plus table MES database with no documentation or DBA support, fully mapped in under 2 hours; five production analytics dashboards built and deployed in 3 working days.
- **Fernando Rojas** — runs business infrastructure, product vision, and technology execution. Completing Computer Science at Harvard Extension, prior product-scale experience at Disney.

**Founding belief:** Manufacturing AI fails when it is sold by people who have never been inside a factory. Prime AI was built inside one. This belief anchors every piece of copy, every proposal, every sales conversation.

**Buyer:** VP of Manufacturing, VP of Operations, or CTO at a mid-market manufacturer, $100M–$2B revenue, 1–5 plants, uses an MES, has heard about AI for years without seeing it work reliably. Intelligent, skeptical, burned before by consultants who didn't understand their systems.

**Service tiers:**
| Tier | Duration | Price | What it delivers |
|---|---|---|---|
| Prime Diagnostics | 2 weeks | $20,000 | Maps MES schema, builds AI data dictionary, delivers implementation roadmap |
| Prime Build | 10 weeks | $75,000–$150,000 | Full governed AI layer: MCP server, semantic views, security model, validated query catalog, production dashboards |
| Prime Retainer | Ongoing | $5,000–$10,000/mo | Maintains and expands the AI layer as the MES evolves |

**Contact:** hello@primeaiconsultants.com | (805) 216-4651 | Phoenix, AZ

**Competitive positioning:**
- *Large consulting firms* (Deloitte, Accenture, IBM) — brand without depth, $500/hr, slide decks not infrastructure.
- *Generic AI consultancies* — can connect AI to databases but can't tell you which tables to trust or where business logic hides.
- *MES vendors* (Rockwell, Siemens, Aveva) — generic AI features, no understanding of specific configs/customizations.

---

## 2. Brand Voice Rules (non-negotiable — apply to every piece of copy)

**Governing principle:** Write like a person who has been in the room, not someone who read about the room. Every sentence should pass this test: could a 30-year semiconductor manufacturing veteran say this out loud without flinching?

**Voice qualities:** Confident (not hedged), Direct (no filler), Technical (use real terms: MES, semantic layer, governed views — not "manufacturing software" or "AI connection"), Earned (proof before assertion), Serious (not playful/casual).

**NEVER use these words/phrases:**
leverage, synergy/synergistic, unlock value/potential, cutting-edge/bleeding-edge, seamlessly/seamless integration, robust (unless a real spec), best-in-class/world-class/industry-leading, empower/empowers, revolutionize/transform (unless earned), game-changer, delve into, in the realm of, "it is worth noting that", "as an AI language model", "I would be happy to", certainly/absolutely as sentence openers, holistic approach/solution, end-to-end solution, at the end of the day, move the needle, low-hanging fruit, circle back/loop in, going forward, value-add (as adjective), pain points (name the actual pain), use case (in marketing copy).

**NEVER use em dashes.** This is the single most-repeated rule across every skill and critique note — em dashes are treated as the clearest visible signature of AI-written copy. Use a period + new sentence, a comma, a colon, parentheses, or a semicolon instead.

**Numbers:** always prefer specific real numbers over vague adjectives. "400-plus table MES database... fully mapped in under 2 hours" beats "significantly faster."

**Reference companies for tone calibration:** Palantir, Sight Machine, AspenTech, Rockwell Automation.

**Copy patterns:**
- *Declarative statement* — short, no decoration. "We do not build demos. We build infrastructure."
- *Proof-first* — lead with the specific result, explain how second. "400-plus table MES database... fully mapped in under 2 hours."
- *Problem-first* — name what the buyer already feels broken, then solve it.

**Full anti-AI-copy checklist** (run before finalizing any copy): zero em dashes, no banned words, at least one specific number, no "it is worth noting," no "world-class"/"best-in-class," every adjective earned or cut, varied sentence rhythm, strong opening line, a 30-year fab veteran could read it aloud without cringing, active voice, cut the last sentence and see if it's stronger.

---

## 3. Visual Identity

**Color system (use only these + white):**
| Role | Hex | Use |
|---|---|---|
| Primary Dark | `#0A0F1E` | Backgrounds, text — authority, precision |
| Teal Accent | `#00D4B8` | ONE accent element per composition — the AI layer |
| Light Background | `#F2F2F5` | Body sections, light surfaces |
| Secondary Text | `#6B6B7E` | Labels, captions, supporting text |

**Typography:** Geometric/humanist sans-serif. Wordmark: light weight "Prime" + medium weight "AI". Body: DM Sans, Neue Haas Grotesk, or IBM Plex (IBM Plex specifically signals engineering precision for this buyer).

**Logo mark:** Concentric circles representing a semiconductor wafer viewed from above (also described elsewhere as three horizontal bars narrowing to a teal terminal point — both describe the same idea: raw inputs → governed AI semantic layer (teal) → one trusted answer). "CONSULTANTS" in small caps below a thin teal rule.

**Never use:** purple/rainbow gradients, neon, orange, drop shadows, stock photos of robots/brains/neural networks/generic "engineer" stock photography, generic connected-dots AI imagery, anything that reads as "AI startup" rather than "industrial technology company."

**Note:** the live site currently uses a warm neutral (`#F3F2EE`) rather than this navy/teal system — see Section 11. Confirm which is current with Fernando/Antonio before making sweeping color changes.

---

## 4. Website Content Inventory (planning reference)

Source: `Website layout for PrimeAIConsultants.xlsx` (project file). Nav: Home / Services / AI for MES, ERP & CRM / AI for Individuals / Contact us / Company / "3 levels of AI?"

Note: the UX skill notes say the "AI for Individuals" page should be **removed from the nav** — wrong audience, dilutes enterprise positioning. It exists as content but should not be a primary nav item.

**Homepage tagline (planning doc):** "Practical AI for real operations — not just theory" (note: per the em-dash rule, this needs to be rewritten without the dash, e.g. "Practical AI for real operations. Not just theory." The live site has since replaced this with a different headline — see Section 11.)

**9 service categories** (Services sheet): AI Strategy & Advisory, AI Training & Enablement, AI Integration Services (ERP/CRM/MES/SAP/API/MCP), AI-Powered Reporting & Analytics, AI Automation Services, AI Development Services, AI Audits & Optimization, AI Support & Managed Services, Executive & Innovation Services. Each has a service list + benefits list — full detail in the project's xlsx file.

**"3 Levels of AI Adoption" framework:** 1) AI Awareness (exploration, prompt engineering), 2) AI Augmentation (AI in daily workflows, integrated with ERP/CRM/MES), 3) AI Transformation (AI embedded in core operations, enterprise-wide integration).

**AI for MES / ERP / CRM pages:** each follows the same structure — short-term benefits (natural language data access, faster reporting, reduced IT backlog), medium-term (6–18mo: AI-assisted development, intelligent insights, cross-system intelligence, conversational analytics), long-term (18mo+: autonomous intelligence, predictive/decision support, democratization of data access). Full copy is in the project xlsx.

---

## 5. MES + AI Integration Roadmap — 10-Phase Methodology (site's methodology page content)

Technology-agnostic: works with any MES (IntelliFab, Camstar, SAP ME/MII, Siemens Opcenter, Critical Manufacturing, FactoryTalk, Oracle MES, custom) and any AI (Claude, ChatGPT/OpenAI, Copilot, Azure OpenAI, Gemini, Bedrock, private LLMs).

**Reference architecture:** AI Assistant Layer → MCP/REST API/Semantic Middleware Layer → Approved AI Semantic Views → MES Application Services/APIs → SQL/Oracle/Postgres → Shop floor systems.

| # | Phase | Timeline | Key Deliverables |
|---|---|---|---|
| 1 | Discovery & Planning | Wk 1 | MES Functional Map, Stakeholder List, Discovery Plan, Project Charter |
| 2 | Stakeholder Discovery | Wk 1–2 | Interview Notes, Business Process Flows, KPI Catalog, Business Rules List |
| 3 | Database Inventory | Wk 2–3 | Database Inventory, Object Catalog, Table Classification, Data Sources List |
| 4 | Data Model & Relationships | Wk 3–4 | ER Diagram, Relationship Matrix, Key Table List, Data Model Documentation |
| 5 | Application Server Analysis | Wk 4–5 | App Architecture Diagram, Job & Process List, Hidden Logic Document, API Inventory |
| 6 | AI Knowledge Preparation | Wk 5–6 | Data Dictionary, Business Definitions, Join & Filter Guide, Valid Values Catalog |
| 7 | Trusted Data & Semantic Layer | Wk 6–7 | Approved Views, Semantic Layer Definition, Query Catalog, Performance Notes |
| 8 | Security & Governance | Wk 7–8 | Security Model, Access Matrix, Audit Plan, Governance Policy |
| 9 | AI Integration & Pilot Build | Wk 8–9 | Integration Architecture, MCP/API Setup, Pilot Use Case Config, Prompt Library |
| 10 | Validation & Pilot Rollout | Wk 9–10 | Validation Report, Accuracy Metrics, Lessons Learned, Pilot Rollout Plan |

Cross-cutting foundations applied to every phase: stakeholder collaboration, documentation & knowledge management, quality assurance, security by design, performance optimization, continuous improvement.

**Governance rule (core technical/brand commitment, stated explicitly in every audience message):** AI never gets unrestricted access to raw MES tables. Always: AI Assistant → MCP/API Layer → Approved SQL Views (read-only, dedicated AI SQL accounts, query auditing, prompt logging, masked sensitive data, SME approval before production, no AI write-back during pilots).

---

## 6. Website UX/Design — Accumulated Decisions & Critique History

This section captures every specific critique and decision made across prior review rounds so a new agent doesn't repeat fixed mistakes.

**Must never return (fixed before, do not reintroduce):**
- Em dashes anywhere on the site.
- The line "We've built websites for three local contractors" (destroys credibility for this buyer).
- "Individuals" in main nav (wrong audience — dilutes enterprise positioning).
- Visible reCAPTCHA developer scaffolding on the live contact form.
- Generic stock photography (e.g. a generic "workbench" or "engineer" stock photo). Real fab photography or none.

**Fixed in V2, must stay fixed:**
- Hero font weight: light, not heavy/condensed (heavy condensed read as consumer brand).
- Pricing visible on service cards ($20k / $75–150k / $5–10k per month). *(Note: live site currently shows no pricing — see Section 11, confirm before changing.)*
- Full 10-phase methodology documented publicly, not gated behind a form.
- Specific anonymized proof cards (400+ tables, under 2 hours, 5 dashboards in 3 days) kept prominent.
- Antonio's closing quote in regular weight, not italic.

**Open issues as of the last review (V2 → V3 punch list):**
- Typography inconsistency across pages — every H1, body paragraph, and CTA button must be pixel-identical everywhere.
- Service card headings render in a different weight than page headings — normalize.
- "Three horizons" headline on the MES page wraps awkwardly — force one line or three deliberate lines.
- Homepage problem card headline wraps ("Your MES, SAP, and Salesforce don't talk to each other.") — shorten or widen.
- Teal hyperlinks overused in body text on methodology/about pages — link only where it adds real value.
- Five operating-principles cards on the About page sit in an inconsistent 3-2 grid — make it 2-column throughout.
- End-of-methodology CTA is a small centered white card — should be a full-width dark section matching other CTA panels.
- Footer shows "PRIME AI CONSULTANTS" as plain bold text instead of the actual SVG wafer-mark logo.
- Centered body text on the About page origin story — left-align for F-pattern reading.
- Contact form MES/ERP dropdown needs specific platform options: Camstar, SAP ME/MII, Siemens Opcenter, FactoryTalk, SAP ECC, Oracle MES, Other.

**Governing UX research principles (Nielsen Norman Group + industry studies) applied throughout:**
1. First impression forms in ~50ms and is purely visual — the site must read as "industrial technology company" (Palantir/Sight Machine register) before any text is read.
2. Show information before asking for commitment — pricing, methodology, and proof must be visible without gating behind a form/sales call.
3. B2B buyers complete ~70% of their evaluation before contacting sales — every page must fully answer its one core question.
4. F-pattern/Z-pattern reading — headlines and body text left-aligned; only very short (≤5 word) statements should be centered.
5. One primary CTA per page (Book Discovery Call, except Contact = submit form).
6. Typography is a trust signal — one font family, 1–2 weights max, pixel-consistent across every page.
7. Social proof must be industry-specific — generic testimonials/logos convert poorly; the specific proof numbers are what work.
8. B2B buying involves 4–12 stakeholders — the site must simultaneously serve the VP of Manufacturing, the CTO/VP IT, and the CEO/GM.
9. Page speed matters disproportionately for a technical buyer — optimize the roadmap diagram image, check PageSpeed after major updates.
10. Mobile-first check at 375px and 390px widths after every change.

**Page-by-page purpose map:**
- **Homepage** — convince a skeptical VP of Manufacturing in <60s.
- **Methodology page** — prove the methodology is real and tested, not theoretical. Best line on the site: *"It will not."* (in response to "AI will automatically understand manufacturing databases" — keep it).
- **About page** — make Antonio's credibility undeniable, Fernando's role clear, story feel earned not performed.
- **Contact page** — reduce friction. Specific MES/ERP dropdown, "what happens next," Antonio's direct contact, 30-minute framing.
- **AI for MES page** — before/after table, three horizons of change, platform compatibility list, MCP architecture explanation.

---

## 7. Using This With DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek's own open-source agent CLI (developer preview, plugin-based, built on the Cordis framework). Install and run from your own Terminal, launched from inside this folder (`~/prime-ai-consultants-site`):

```bash
npx @deepseek-ai/dsh web
```

Get a DeepSeek API key at platform.deepseek.com first. Launches a local web UI at `http://127.0.0.1:3080`.

DeepSeek Harness is in developer preview with breaking changes expected.

**For broader Prime AI business context (Supabase control plane, CRM/relationship pipeline, internal agent roster) that doesn't belong in this deployed repo, see `~/prime-ai-consultants-ops/AGENTS.md`.**

---

## 8. Website V3 Punch List (most actionable next work)

- Typography consistency across all pages (biggest open item — see Section 6).
- Homepage tagline currently contains an em dash and needs a rewrite per the voice rules (or confirm the live site's new hero headline replaces it entirely).
- A named client reference (even one) was flagged as the single highest-impact trust addition once available.
- A dedicated CTO/security one-pager was flagged as missing.

---

## 9. Live Website

**URL:** https://www.primeaiconsultants.com/

As of August 17, 2026, the live site has diverged from the planning content in Sections 4 and 8 (which reflect the `Website layout for PrimeAIConsultants.xlsx` planning document and prior critique rounds). Treat the live site as current source of truth for what's actually published.

Observed on the live site:
- Nav: Home, Diagnostics, Methodology, Services (AI for MES / AI for ERP / AI for CRM), About Us, Contact. Primary CTA: "Discuss your environment."
- Hero headline: **"Know Your Operation Before You Trust AI."** Subhead theme: "Write the operation down first." Sharper, more specific expression of the governance pillar than the planning doc's tagline. Good copy, worth preserving.
- Current service framing: **Prime Diagnostics**, **Architecture & Pilot Definition**, **Implementation Support** — differs from the "Diagnostics / Build / Retainer" three-tier framing in Section 1. Confirm which framing is current before writing new copy or proposals.
- No pricing currently displayed on the live site, despite the "pricing should be visible" UX principle. Confirm with Fernando/Antonio whether hiding it was deliberate.
- Color theme observed: a warm neutral (`#F3F2EE`), not the navy/teal system in Section 3.
- Strong line worth preserving: "The model isn't the first problem. The data is usually there; the meaning often isn't."

Fetch the live site fresh before doing further work rather than relying only on this file — it's being updated outside of this document (this repo has `scripts` and `UPDATE_REPORTS` folders suggesting some automation already touches it; check those before assuming manual-only edits).
