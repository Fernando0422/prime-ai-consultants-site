# Prime AI Consultants — Site Audit

Generated for external copy review and component reorganization planning. **Documentation only** — reflects repository state at audit time.

---

## Section 1 — Page Inventory

### Live routes (served via Vercel static hosting + `vercel.json` clean URLs)

| Route | File | Purpose | In main nav? |
|-------|------|---------|--------------|
| `/` | `index.html` | Marketing homepage — hero, proof, services preview, methodology, team, Ai4, FAQ, CTAs | Yes |
| `/methodology` | `methodology.html` | Full 10-phase governed AI framework (MES reference + cross-industry framing) | Yes |
| `/services` | `services.html` | Three engagements (Diagnostics, Build, Retainer) + solution surfaces | Yes |
| `/ai-mes` | `ai-mes.html` | Vertical landing: AI for manufacturing / MES | No (Services dropdown → Solutions + footer) |
| `/ai-erp` | `ai-erp.html` | Vertical landing: AI for ERP / finance ops | No (Services dropdown → Solutions + footer) |
| `/ai-crm` | `ai-crm.html` | Vertical landing: AI for CRM / revenue ops | No (Services dropdown → Solutions + footer) |
| `/company` | `company.html` | About, principles, team bios | Yes |
| `/contact` | `contact.html` | Discovery call scheduling + contact form | Yes |
| `/privacy` | `privacy.html` | Privacy policy (starter legal) | No (footer legal links only) |
| `/terms` | `terms.html` | Terms of service (starter legal) | No (footer legal links only) |

**Nav structure (desktop ≥921px):** Home · Methodology · Services (dropdown: All Services, Prime Diagnostics, Prime Build, Prime Retainer, Solutions → AI for MES/ERP/CRM) · About · Contact · Book Discovery Call (button)

**Mobile nav:** Same links + Book Discovery Call in drawer.

### Redirects (`vercel.json`)
- `/ai-individuals` → `/services` (301 permanent)
- `/ai-individuals.html` → `/services` (301 permanent)
- `/levels-of-ai` → `/methodology` (301 permanent)
- `/levels-of-ai.html` → `/methodology` (301 permanent)

### Non-route source files
- `page_content/*.frag.html` — legacy/build fragments used by `scripts/render_pages.py`; **not** served as live routes
- `scripts/render_pages.py` — stale generator; live pages are hand-maintained

### Shared global chrome (duplicated per page)
- Skip link: `Skip to main content`
- Ai4 toast (sitewide): tag `Ai4 2026`, body copy, `Book a meeting`, `Details`, dismiss
- Sticky CTA (sitewide): `Book Discovery Call`
- Footer: brand tagline, Services/Methodology/Connect columns, statement, copyright, Privacy/Terms

---

## Section 2 — Copy Extraction (verbatim)

> Copy below is extracted from HTML source in document order. `<br>` becomes a space in flattened text. Entity references are decoded to literal characters.

### Page: /  (index.html)

[Page title] Prime AI Consultants · Governed AI on Operational Data
[Meta description] Governed AI on legacy operational databases — MES, ERP, and custom apps. Meet Prime AI at Ai4 Las Vegas Aug 4–6. Start with a 2-week diagnostic.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] Governed AI on Operational Data
[Eyebrow] Governed AI on
[Eyebrow] Operational Data
[H1] Your Operations Data
[Body] We map legacy databases, build a governed semantic layer, and deploy AI your engineers validate — without replacing your MES, ERP, or core systems. Weeks, not an 18-month transformation program.
[Body] Governed AI on MES, ERP, and custom operational databases.
[CTA Button] Book Free Discovery Call
[CTA Button] Start with 2-Week Diagnostic

[Section: pitch-video]
[Eyebrow] Overview
[H2] Governed AI on operational data — in 90 seconds
[Body] How we map legacy databases, build a semantic layer your SMEs validate, and deploy AI on read-only approved views — without replacing MES, ERP, or core systems.
[Body] Prefer to read? See the elevator pitch
[Body] Video plays when assets/hero/pitch-90s.mp4

[Section: Trust indicators]

[Section: ai4]
[H2] Meet Prime AI at America’s largest AI conference
[Body] Antonio and Fernando will be at Ai4 Aug 4–6 at The Venetian. If your AI pilot stalled because teams don’t trust answers from raw operational data, let’s compare notes.
[CTA Button] Book time at Ai4
[CTA Button] Schedule discovery call
[Body] Elevator pitch
[Body] We map legacy operational databases, build a governed semantic layer your SMEs validate, and deploy AI on read-only approved views — without replacing MES, ERP, or core systems. Start with a 2-week diagnostic.

[Section: Why teams work with us]
[Body] Years enterprise systems experience on the founding team
[Body] Prime Diagnostics — low-risk entry before any major build
[Body] Read-only database access with full query audit trail
[Body] Code, dictionary, and semantic layer stay with you — no lock-in
[Body] We’re a focused boutique. Founder credibility and a productized diagnostic de-risk your first engagement.

[Section: industries]
[Eyebrow] Where this applies
[H2] Same governed playbook.
[Body] Pick your industry — see how we map legacy data, govern access, and deploy AI your teams can defend.
[H3] Manufacturing & MES
[List item] Yield, WIP, and equipment logic across hundreds of tables — often undocumented
[List item] Governed views and read-only AI access your engineers validate
[List item] Platform-agnostic: Camstar, SAP ME, Opcenter, FactoryTalk, custom MES
[Body] Typical entry: Prime Diagnostics

[Section: Footer]
[CTA Button] Explore AI for MES
[H3] Healthcare & life sciences
[List item] Clinical and operational datasets with strict governance requirements
[List item] AI routed through approved views — traceable, SME-validated, audit-ready
[List item] Map schema and tribal knowledge before any model touches production
[Body] Same playbook as manufacturing: inventory, govern, then deploy.

[Section: Footer]
[CTA Button] Talk about your environment
[H3] Financial services
[List item] Reconciliation rules and custom ERP fields AI cannot infer from schema alone
[List item] Documented semantics before models query operational or finance data
[List item] Trustworthy daily views for finance and ops — without replacing your ERP
[Body] Built for teams that need defensible numbers, not another dashboard experiment.

[Section: Footer]
[CTA Button] Explore AI for ERP
[H3] Energy & utilities
[List item] Asset, grid, and operations data across SCADA exports, historians, and ERP
[List item] Unified operational picture under governed read-only access
[List item] No AI on raw operational tables until views are approved
[Body] For environments where safety and auditability come first.

[Section: Footer]
[CTA Button] Talk about your environment
[H3] Retail & supply chain
[List item] Inventory, fulfillment, and order data split across ERP, WMS, and custom apps
[List item] Relationship mapping and approved views for AI and analytics
[List item] Faster answers on stock, orders, and exceptions — with signed-off logic
[Body] Reduce admin bottlenecks without ripping out systems of record.

[Section: Footer]
[CTA Button] Talk about your environment
[H3] Enterprise ERP & custom apps
[List item] Operational apps and warehouses nobody fully documented
[List item] Table inventory plus tribal knowledge captured in a semantic layer
[List item] Your stack stays — we add the governed intelligence layer on top
[Body] When “we have an ERP” still means hundreds of undocumented tables.

[Section: Footer]
[CTA Button] See how we engage

[Section: section]
[Eyebrow] How We Help
[H2] Outcomes your AI initiative actually needs.
[Body] Not another chatbot on raw tables. Infrastructure your operators and data teams can defend.
[H3] Trustworthy AI answers
[Body] Governed semantic layer between your LLM and approved read-only views — traceable, SME-validated, explainable.
[H3] Faster operational decisions
[Body] Engineers and analysts get answers in minutes instead of hours of SQL pulls and spreadsheet reconciliation.
[H3] You own what we build
[Body] Data dictionary, views, governance docs, and code — no subscription required to keep using your layer.

[Section: section]
[Eyebrow] What We Build
[H2] Governed infrastructure — not a chatbot on raw tables.
[Body] Whether you’re evaluating agents, RAG, or governance, this is the data trust layer underneath.
[H3] AI data dictionary
[Body] Business meaning for tables, views, and calculations — the context LLMs cannot infer from schema alone.
[H3] Governed semantic layer
[Body] Approved read-only views with business logic baked in — your RAG surface and agent query boundary.
[H3] Query audit trail
[Body] Every AI question logged — traceable to views, calculations, and the SME who validated them.
[H3] SME validation gates
[Body] Engineers sign off before production use — so stalled pilots become trusted daily workflows.

[Section: governed-architecture]
[Eyebrow] Prime Build
[H2] Governed access — or no access.
[Body] AI never touches raw operational tables. Every query routes through a semantic layer and read-only approved views your SMEs validate.

[Section: section]
[Eyebrow] How We Work
[H2] The governed AI path on operational data.
[Body] Four phases — from first conversation to infrastructure your team owns. Most teams enter at Prime Diagnostics.
[List item] 01
[List item] 02
[List item] 03
[List item] 04
[Body] While enterprise programs spend 18 months in planning,

[Section: stats]
[Eyebrow] Typical Results
[H2] Representative outcomes from governed engagements.
[Body] Operational tables mapped in weeks, not months
[Body] Typical for MES-scale schemas (400+ tables). Timeline varies by system.
[Body] Working days to build semantic layer from scratch
[Body] After database inventory is complete.
[Body] Production dashboards deployed within 10 days
[Body] Validated by engineers before use.
[Body] Typical implementation timeline
[Body] Depends on schema complexity and team availability.
[Body] Based on representative engagements. Your timeline may vary.

[Section: section]
[Eyebrow] The Real Problem
[H2] Legacy operational databases were not built for AI.
[Body] MES, ERP, and custom apps were built for transactions — with business logic buried in stored procedures, years of customizations, undocumented schemas, and tribal knowledge only a few people understand.
[Body] Connect AI directly to those tables and you get unreliable answers. Operators and engineers stop trusting the system. The pilot stalls.
[Body] The issue isn’t the technology.
[Body] The issue is that nobody mapped the database before plugging in the AI.

[Section: section]
[Eyebrow] The Operator’s Mindset
[H2] Built by operators who’ve run the systems — not adapted from a generic AI playbook.
[Body] Prime AI exists because Antonio spent 18 years inside semiconductor and discrete manufacturing running MES and production systems. He knows where operational logic hides, why teams don’t trust raw-table answers, and what “governed” has to mean before AI goes live.
[Body] We don’t sell demos. We map your database, build the layer, and leave you with infrastructure your SMEs can defend — whether you’re in manufacturing, ERP-heavy finance, or enterprise IT.
[CTA Button] Meet the team

[Section: section]
[Eyebrow] Three Differences
[H2] Why Prime AI delivers where others demo.
[H3] Governed access, or none
[Body] We don’t connect AI
[CTA Button] See the architecture diagram ↓
[H3] Built by Operators, Not Slide Decks
[Body] 30+ years enterprise systems on the founding team; deepest track record in manufacturing and MES. The same governed playbook applies to ERP, healthcare operations, financial ops, and custom enterprise apps.
[List item] Large operational schemas mapped in weeks, not months
[List item] Semantic layer built in 3–5 working days
[List item] Five production dashboards live within 10 days
[List item] AI answers
[Body] Timelines vary by schema complexity and team availability.
[H3] You Own Everything We Build
[Body] When the engagement ends, the code, documentation, data dictionary, and semantic layer are yours. No vendor lock-in, no subscription to keep using what we built.
[Body] We prefer clients who can run without us—because those clients trust us enough to bring us back.

[Section: section]
[Eyebrow] Why Prime AI
[H2] How we compare to the usual options.
[Body] You don’t need another horizontal “AI for any business” vendor. You need governed infrastructure on the data you already run.
[Body] Most clients start with Prime Diagnostics

[Section: engage]
[Eyebrow] What We Offer
[H2] Three engagements.
[Body] Where should you start?
[Body] 2-week database inventory and data dictionary before any AI work.
[Body] ~10-week semantic layer design, build, and governed deployment.
[Body] Ongoing optimization, new views, and strategic guidance.
[Body] Most teams start with Prime Diagnostics
[H3] Prime Diagnostics
[Body] The Foundation
[Body] Map your operational database before touching AI
[Body] What happens:
[List item] Inventory tables, views, procedures, and relationships
[List item] Classify by business area and flag sensitive data
[List item] Build a first-draft AI data dictionary with business meaning
[List item] Define what “trusted source” means in your org
[Body] Result:
[CTA Button] Start with Diagnostics
[H3] Prime Build
[Body] The Implementation
[Body] Design, build, and deploy governed semantic views and access controls.
[Body] What happens:
[List item] Design semantic views for priority analytics questions
[List item] Build read-only semantic layer with audit logging
[List item] Train your team and deploy with full documentation
[Body] Result:
[CTA Button] Start with Prime Build
[H3] Prime Retainer
[Body] The Partnership
[Body] Continuous optimization and capability expansion as operations evolve.
[Body] What happens:
[List item] Quarterly semantic layer and governance reviews
[List item] 1–2 new semantic views per quarter
[List item] On-call support via dedicated Slack channel
[Body] Result:
[CTA Button] Get Started

[Section: section]
[Eyebrow] Case Studies
[H2] Representative outcomes from governed operational data work.
[Body] Composite case patterns — not attributed to a named public client.
[H3] Why trust us without a logo wall?
[Body] We’re a boutique. Antonio’s 18 years on the shop floor grounds our manufacturing work; the same governance model applies wherever legacy operational data blocks trusted AI. Prime Diagnostics lets you validate the approach in two weeks — with deliverables you keep regardless.
[Body] 6–8 hrs/week → minutes per query
[Body] Reducing Engineer Time Spent on Data Pulls
[Body] Engineers answer operational questions in minutes instead of hours. Data is consistent org-wide.
[Button] Read full story ▼
[Body] The situation
[Body] Mid-market discrete manufacturer. Engineers spent 6–8 hours weekly pulling MES data and reconciling spreadsheets.
[Body] The problem
[Body] 400+ tables, no documentation, no trusted relationships. Engineers didn’t trust the data.
[Body] What we did
[List item] Mapped schema and built a data dictionary
[List item] Identified 12 core tables covering 90% of questions
[List item] Built five semantic views with read-only access and query logging
[List item] Trained the team on governance
[Body] The result
[Body] Questions answered in minutes. Consistent data org-wide. No spreadsheet reconciliation.
[Body] Time to implementation:
[Body] Stalled AI project → trusted daily use
[Body] Building Trust in AI-Generated Insights
[Body] Engineers trust AI insights because they understand how answers are calculated.
[Button] Read full story ▼
[Body] The situation
[Body] Food manufacturer wanted AI for yield and defect analysis. Generic tools produced answers engineers didn’t trust.
[Body] The problem
[Body] AI connected directly to production tables. Answers contradicted engineer ground truth. The project stalled.
[Body] What we did
[List item] Audited setup and surfaced hidden logic in stored procedures
[List item] Rebuilt semantic layer with explicit calculation rules
[List item] Added validation gate for every AI question
[List item] Documented the layer so anyone can follow the logic
[Body] The result
[Body] Trusted insights for root cause analysis and process optimization.
[Body] Outcome demonstrated across similar process manufacturing environments.
[Body] Days of reconciliation → governed daily views
[Body] Trustworthy Numbers Without Replacing ERP
[Body] Finance and ops teams query approved semantic views instead of rebuilding spreadsheets from raw extracts.
[Button] Read full story ▼
[Body] The situation
[Body] Regional financial operator on a heavily customized ERP. Month-end and ops reporting required manual pulls, pivot tables, and email chains.
[Body] The problem
[Body] Leadership wanted AI-assisted analysis, but calculation rules lived in reports, macros, and tribal knowledge — not in a model the LLM could safely use.
[Body] What we did
[List item] Inventory and dictionary for core finance and ops tables
[List item] Semantic views with documented reconciliation logic
[List item] Read-only access and query audit for every AI request
[List item] SME sign-off on definitions before production use
[Body] The result
[Body] Trusted daily and weekly views; AI answers trace back to approved calculations — without an ERP replacement project.
[Body] Composite pattern from similar ERP-heavy operational environments.
[Body] Composite patterns from similar operational environments — not attributed to a named client. Results depend on schema complexity, SME availability, and adoption.

[Section: section]
[Eyebrow] What You See
[H2] Visibility into every table, relationship, and governance decision.
[Body] Prime Diagnostics produces a living data dictionary — not a slide deck. Prime Build turns that into semantic views your team queries daily.
[Body] You see what exists, what it means, what’s sensitive, and what to build next — with full audit logging and SME sign-off before production.
[CTA Button] View 10-phase methodology

[Section: section]
[Eyebrow] Our Methodology
[H2] How we work: a typical 10-week implementation.
[CTA Button] View full 10-phase roadmap
[Body] Typical for 400–800 table schemas. Actual timeline depends on schema size, data access, and SME availability.
[Body] Phase-level detail and cross-cutting foundations live on our Methodology page.

[Section: platform-wall-heading]
[Eyebrow] Systems We Map
[H2] The intelligence is in the methodology — not the logo.
[Body] We’ve modeled and deployed against major MES, ERP, and AI platforms. Your stack stays yours; we build the governed layer on top.

[Section: solutions]
[Eyebrow] Where We Plug In
[H2] Governed AI across your operations stack.
[Body] Same methodology — applied where your operational truth lives.

[Section: team]
[Eyebrow] The Team
[H2] The people who built the methodology.
[H3] Antonio Rojas
[Body] 30 years of enterprise systems experience, including 18 years inside semiconductor and discrete manufacturing—building, debugging, and improving the systems that ran production. He knows why MES databases are structured the way they are and where business logic hides.
[Body] The Prime AI rule: operational databases need context before they can serve AI. Every engagement starts with your systems, constraints, and definition of truth.
[H3] Fernando Rojas
[Body] Fernando builds the infrastructure that turns manufacturing expertise into a scalable business—spanning product, engineering, and how those two should talk to each other. He holds a Bachelor of Science in Web Design and Engineering from Santa Clara University and is pursuing a Master’s in Computer Science through Harvard Extension School.
[Body] Background includes enterprise platforms at Disney and product-scale work at La Mer (Estée Lauder). At Prime AI, he turns deep operations expertise into repeatable, governed delivery.

[Section: who-its-for]
[Eyebrow] Who it’s for
[H2] Operational data trust — not every AI project.
[Body] We’d rather be clear on fit than chase the wrong conversation.
[H3] Strong fit
[List item] VP Ops, plant IT, data engineering, or enterprise architecture
[List item] Legacy MES, ERP, or custom ops database (often 100+ tables)
[List item] AI pilot stalled because SMEs don’t trust raw-table answers
[List item] Need read-only governance, audit trail, and deliverables you own
[List item] Ops-heavy startups (logistics, hardware, bio, fintech cores) with real production data
[H3] Maybe — worth a call
[List item] Modern cloud warehouse only — no operational system of record yet
[List item] Early-stage team exploring AI but no database to govern
[List item] Want us to build a customer-facing chatbot on your marketing site
[Body] We’ll tell you honestly if Prime Diagnostics is the right first step.
[H3] We’ll point you elsewhere
[List item] Generic “automate my business with ChatGPT” with no ops database
[List item] Horizontal workflow tools with no legacy data problem
[List item] 18-month transformation RFPs without a defined schema to map
[Body] Horizontal AI vendors and Big 4 programs may be a better match.

[Section: faq]
[Eyebrow] FAQ
[H2] Questions we hear in discovery calls.
[Body] Manufacturing is our deepest credibility — especially MES. The same governed playbook applies to ERP, healthcare operations, financial ops, and custom enterprise apps. If your AI initiative depends on messy legacy operational data, we can help.
[Body] If you have a real operational database (production, logistics, finance ops) and need governed AI on it, we can help. If you only need a product copilot or doc RAG on SaaS tools, we’re usually not the right fit — and we’ll say so on the discovery call.
[Body] Platforms give you access. They don’t map your stored procedures, custom fields, or tribal knowledge. We build the semantic layer and governance your team needs to trust answers — on top of what you already own.
[Body] Table inventory, relationship map, first-draft AI data dictionary, sensitive-data flags, and a prioritized roadmap. You keep everything — it’s yours even if you don’t continue to Prime Build.
[Body] Read-only database access, approved views only, query logging, and SME validation gates before production use. We align with your IT and compliance team — not around them.
[Body] Yes. Antonio and Fernando attend Aug 4–6, 2026 at The Venetian, Las Vegas. Book time

[Section: readiness]
[Eyebrow] Free resource
[H2] AI Readiness Checklist for Operational Data
[Body] Eight questions to ask before connecting an LLM to MES, ERP, or custom databases — plus what “governed” actually means in practice.
[List item] Schema inventory vs. business meaning
[List item] Where calculation logic actually lives
[List item] SME validation before production
[List item] Read-only access and audit requirements
[Body] Request the checklist on your discovery call — we’ll walk through it together.
[CTA Button] Get the checklist

[Section: feature-band-heading]
[Eyebrow] Start Low-Risk
[H2] Map your database in two weeks. Then decide.
[Body] Prime Diagnostics gives you a data dictionary, relationship map, and roadmap — deliverables you keep even if you don’t continue. No 18-month program. No platform lock-in.
[CTA Button] Book free discovery call

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run — MES, ERP, and custom apps. Manufacturing is our deepest proof; the playbook applies wherever legacy data blocks trusted AI.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Ai4 2026 · Las Vegas
[List item] Who we’re for
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /methodology  (methodology.html)

[Page title] Methodology · The Prime AI 10-Phase Framework
[Meta description] 10-phase governed AI framework for operational data — MES, ERP, CRM, and custom apps. Map the database, build the semantic layer, deploy AI your team trusts. Meet us at Ai4 Las Vegas.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] Our Methodology
[H1] The 10-phase framework for governed AI on operational data.
[Body] Map legacy databases, build a semantic layer your SMEs validate, deploy AI on read-only approved views. Ten weeks from discovery through pilot.
[List item] MES
[List item] ERP
[List item] CRM
[List item] Custom databases
[CTA Button] Book Discovery Call
[CTA Button] See the roadmap →

[Section: method-intro-heading]
[Eyebrow] Why This Methodology Exists
[H2] The biggest mistake in AI + ops data
[Body] Assuming AI will automatically understand your operational database and business logic — whether that’s MES, ERP, CRM, or a custom system of record.
[Body] It will not.
[H3] What usually happens
[List item] Consultants connect AI to raw operational tables
[List item] Answers follow table names and column patterns
[List item] Results don’t match how SMEs know the system works
[List item] Trust collapses — the project stalls
[H3] Why raw tables fail
[Body] Operational databases were built for transactions and workflows — not for AI. Business logic lives in stored procedures, integrations, and years of undocumented customization.
[Body] Tables hold data. They don’t hold context.
[H3] What has to exist first
[List item] What each table represents
[List item] Which joins are valid
[List item] Logic hidden in procedures
[List item] Which answers actually matter to operations

[Section: Footer]
[Body] This methodology builds that semantic layer before
[CTA Button] See the 10 phases

[Section: framework-applies]
[H2] One framework. MES, ERP, and CRM.
[Body] The phase structure is identical. Examples and SME language change by system — not the sequence.

[Section: framework]
[Eyebrow] The 10-Phase Framework
[H2] From unknown database to trusted intelligence layer.
[Body] Ten phased weeks from discovery through pilot rollout. Same sequence for MES, ERP, CRM, and custom operational databases — see vertical entry points
[Body] Governed AI Roadmap
[Body] ←
[H3] Discovery & Planning
[Body] Key activities
[List item] Business objectives
[List item] Operational domains mapped
[List item] Stakeholders mapped
[List item] Discovery approach planned
[Body] Deliverables
[List item] Domain & data map
[List item] Stakeholder List
[List item] Discovery Plan
[List item] Project Charter
[H3] Stakeholder Discovery
[Body] Key activities
[List item] SMEs, developers, DBAs
[List item] Key reports & KPIs
[List item] Business rules documented
[Body] Deliverables
[List item] Interview Notes
[List item] Process flows
[List item] KPI Catalog
[List item] Business Rules List
[H3] Database Inventory
[Body] Key activities
[List item] Tables, views, procedures
[List item] Triggers, jobs, indexes
[List item] Classification by role
[List item] Identify key databases
[Body] Deliverables
[List item] Database Inventory
[List item] Object Catalog
[List item] Table Classification
[List item] Data Sources List
[H3] Data Model & Relationships
[Body] Key activities
[List item] Keys & relationships
[List item] Documented vs inferred links
[List item] ER diagrams & entity flow
[Body] Deliverables
[List item] ER Diagram
[List item] Relationship Matrix
[List item] Key Tables
[List item] Model documentation
[H3] Application Server Analysis
[Body] Key activities
[List item] App architecture review
[List item] APIs & services
[List item] Jobs, logs, configuration
[Body] Deliverables
[List item] Architecture diagram
[List item] Job & Process List
[List item] Hidden logic doc
[List item] API inventory
[H3] AI Knowledge Preparation
[Body] Key activities
[List item] Data dictionary
[List item] Columns, values, definitions
[List item] Joins, filters, rules
[List item] Sensitive data flagged
[Body] Deliverables
[List item] Data Dictionary
[List item] Business Definitions
[List item] Join & Filter Guide
[List item] Valid Values Catalog
[H3] Trusted Data & Semantic Layer
[Body] Key activities
[List item] AI-approved views only
[List item] Trusted query definitions
[List item] Performance tuned
[Body] Deliverables
[List item] Approved views
[List item] Semantic layer spec
[List item] Query catalog
[List item] Performance notes
[H3] Security & Governance
[Body] Key activities
[List item] Read-only access model
[List item] Roles & permissions
[List item] Privacy & audit logging
[List item] Approval workflow
[Body] Deliverables
[List item] Security model
[List item] Access matrix
[List item] Audit plan
[List item] Governance policy
[H3] AI Integration & Pilot Build
[Body] Key activities
[List item] MCP / API bridge
[List item] Semantic layer wired
[List item] Approved data only
[List item] Pilot use cases live
[Body] Deliverables
[List item] Integration architecture
[List item] MCP / API setup
[List item] Pilot configuration
[List item] Prompt library
[H3] Validation & Pilot Rollout
[Body] Key activities
[List item] Test question library
[List item] Answers vs trusted reports
[List item] SME sign-off gates
[Body] Deliverables
[List item] Validation report
[List item] Accuracy metrics
[List item] Lessons learned
[List item] Pilot rollout plan
[Body] Cross-cutting foundations, every phase
[H3] Stakeholder collaboration
[Body] Continuous SMEs, DBAs, developers & users.
[H3] Documentation
[Body] Central repository for every finding & decision.
[H3] Quality assurance
[Body] Review deliverables against standards.
[H3] Security by design
[Body] Privacy & access from day one.
[H3] Performance
[Body] Models & views tuned for production scale.
[H3] Continuous improvement
[Body] Iterate with feedback loops.
[Body] Outcome
[Body] A trusted AI foundation for your operational data.
[Body] Same governed intelligence layer whether your system is MES, ERP, CRM, or custom.
[Body] Semantic understanding of business meaning, structure, relationships, and logic.
[Body] Ready for accurate, reliable insights.

[Section: phases]
[Eyebrow] Phase Detail
[H2] Inside every phase.
[Body] What we do. Why it matters. What you walk away with.
[Body] System-agnostic by design — MES, ERP, CRM, or custom operational databases. Pick your vertical
[Button] 01
[H3] Discovery & Planning
[Body] Before a single database query, we map the business problems you need solved, which operational domains and data areas matter most, who the stakeholders are, and how discovery will run.
[Body] Most AI projects jump straight to connecting the database. That fails because nobody asked what questions your team actually needs answered. This is the only phase where we are not touching the database. We understand your business first.
[List item] Domain & data map
[List item] Stakeholder List
[List item] Discovery Plan
[List item] Project Charter
[Button] 02
[H3] Stakeholder Discovery
[Body] We interview SMEs, developers, DBAs, and business users. We identify key reports, KPIs, and business rules. We capture the tribal knowledge that lives in people’s heads, not in any documentation.
[Body] The most important information about your operational system is not in the database. It is in the people who use it every day. We find them and document them.
[List item] Interview Notes
[List item] Business Process Flows
[List item] KPI Catalog
[List item] Business Rules List
[Button] 03
[H3] Database Inventory
[Body] Using MCP-connected AI discovery, we inventory every table, view, stored procedure, trigger, and SQL job. We classify table types (master, transaction, history, summary) and identify key databases. No manual queries required.
[Body] Large operational schemas often have hundreds of tables with little documentation. On typical engagements we fully inventory schemas in weeks, not months. This phase replaces slow manual discovery with a systematic, governed process.
[List item] Database Inventory
[List item] Object Catalog
[List item] Table Classification
[List item] Data Sources List
[Button] 04
[H3] Data Model & Relationships
[Body] We identify primary and foreign keys, detect documented and undocumented relationships, build ER diagrams, and map how entities flow through your business (orders, lots, accounts, inventory — whatever your domain uses). Legacy systems often lack formal foreign keys, so hidden relationships must be inferred from stored procedures, naming conventions, and application traces.
[Body] AI cannot join tables it does not understand. This phase gives the AI the relational map it needs to answer multi-table questions correctly.
[List item] ER Diagram
[List item] Relationship Matrix
[List item] Key Table List
[List item] Data Model Documentation
[Button] 05
[H3] Application Server Analysis
[Body] We review application architecture, analyze APIs and services, review configuration files, analyze scheduled jobs, and review application logs. We identify hidden calculations and status transitions that the database alone does not reveal.
[Body] Critical business logic does not live entirely in the database. Scheduled jobs transform data. Middleware and app services recalculate values. If AI does not know this, it will answer questions about stale or transformed data incorrectly.
[List item] App Architecture Diagram
[List item] Job & Process List
[List item] Hidden Logic Document
[List item] API Inventory
[Button] 06
[H3] AI Knowledge Preparation
[Body] We create the AI data dictionary, documenting table purpose, columns, valid values, business definitions, joins, filters, and rules. We identify sensitive data and build the trusted query catalog that governs every AI interaction.
[Body] This is the semantic layer between raw data and AI understanding. Without it, AI answers are unreliable. With it, AI consistently answers operational questions the way your SMEs expect.
[List item] AI Data Dictionary
[List item] Business Definitions
[List item] Join & Filter Guide
[List item] Valid Values Catalog
[Button] 07
[H3] Trusted Data & Semantic Layer
[Body] We design AI-approved views, create the semantic layer, define trusted queries, build the query catalog, and optimize for performance. No AI query ever touches raw operational tables directly.
[Body] This is the architectural decision that separates AI implementations that work from ones that fail. Governed views mean governed answers. Raw table access means hallucinations and trust collapse.
[List item] Approved views (governed vw_AI_* per domain)
[List item] Semantic Layer Definition
[List item] Query Catalog
[List item] Performance Notes
[Button] 08
[H3] Security & Governance
[Body] We define read-only access models, create SQL roles and permissions, define data privacy rules, set up audit logging, and establish the approval workflow for new AI use cases.
[Body] Operational data is sensitive — production metrics, financial figures, pipeline and customer data. Governance is not an afterthought. It is built from day one.
[List item] Security Model
[List item] Access Matrix
[List item] Audit Plan
[List item] Governance Policy
[Button] 09
[H3] AI Integration & Pilot Build
[Body] We build the MCP/API layer, connect the AI assistant to the semantic layer, configure prompts and tools, restrict AI to approved data, and build the first pilot use cases.
[Body] This is where the methodology becomes a working product. Your team asks questions in plain language and gets answers they trust, with lineage back to the source data.
[List item] Integration Architecture
[List item] MCP/API Setup
[List item] Pilot Use Case Configuration
[List item] Prompt Library
[Button] 10
[H3] Validation & Pilot Rollout
[Body] We create test questions, validate AI answers against known reports, measure accuracy, refine views and rules, and get SME sign-off. No AI reaches end users without human expert validation.
[Body] One wrong number on a trusted KPI drives a bad decision. Trust, once lost, is hard to rebuild. Validation is not optional.
[List item] Validation Report
[List item] Accuracy Metrics
[List item] Lessons Learned
[List item] Pilot Rollout Plan
[Body] Outcome
[Body] A trusted AI foundation for your operational data.
[Body] Same governed intelligence layer whether your system is MES, ERP, CRM, or custom.
[Body] Semantic understanding of business meaning, structure, relationships, and logic.
[Body] Ready for accurate, reliable insights.
[H3] Methodology Timeline Note
[Body] This timeline is typical for 400–800 table schemas with moderate complexity. Actual timeline depends on your schema size, data access constraints, and SME availability. Prime AI’s 10-phase engagement will be refined and confirmed after Prime Diagnostics.

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[List item] Ai4 2026 · Las Vegas
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /services  (services.html)

[Page title] Services · Prime AI Consultants
[Meta description] Prime Diagnostics (2 weeks), Prime Build (~10 weeks), Prime Retainer. Governed AI on MES, ERP, and operational data. Most clients start with the diagnostic.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] How We Engage
[H1] Prime Diagnostics, Prime Build, Prime Retainer.
[Body] Governed AI on operational data you already run — MES, ERP, custom apps. Map the database first. Build the semantic layer. Deploy AI your team trusts.
[Body] Most engagements start with Prime Diagnostics
[CTA Button] Start with Diagnostics
[CTA Button] See the 10 phases

[Section: section]
[Body] Prime Diagnostics maps what you have. Prime Build puts governed AI in production. Prime Retainer keeps the layer current as your operations change.
[Body] Typical timelines below. Exact scope confirmed after discovery.

[Section: services-engage-heading]
[H2] Engagement options
[H3] Prime Diagnostics
[Body] Phase 1 discovery.
[Body] Typical outcomes:
[List item] 400+ table database fully inventoried
[List item] Hidden relationships identified and mapped
[List item] Data dictionary created
[List item] Business area classification (WIP, Yield, Equipment, etc.)
[List item] Sensitive data identified and classified
[List item] Top 20 important tables/views documented
[List item] Governance foundation established
[Body] This phase answers: “What do we actually have? How does it work? Where should AI focus?”
[CTA Button] Schedule a Call
[H3] Prime Build
[Body] Design, build, deploy, and validate the semantic layer and governed access framework.
[Body] Typical outcomes:
[List item] 5–7 AI-approved semantic views in production
[List item] Complete data dictionary with business definitions
[List item] Governance policy (read-only access, query logging, audit trail)
[List item] Access control rules and query audit framework
[List item] Team training (4–6 hours)
[List item] 30-day post-launch support
[Body] Timeline:
[CTA Button] Learn More
[H3] Prime Retainer
[Body] Continuous optimization, new capabilities, and strategic guidance.
[Body] Typical outcomes:
[List item] Quarterly business reviews
[List item] 1–2 new semantic views per quarter
[List item] Performance optimization
[List item] Governance policy updates
[List item] Team training on new capabilities
[List item] Slack channel for quick questions
[List item] Custom capability development
[CTA Button] Get Started

[Section: section]
[Eyebrow] Where We Work
[H2] One methodology.
[Body] The same governed AI architecture, applied to the system that matters most to you.
[H3] AI for MES
[Body] Manufacturing intelligence at the speed of a question. Yield, WIP, equipment, cycle time, answered without SQL tickets.
[CTA Button] Explore AI for MES
[H3] AI for ERP
[Body] Conversational access to SAP, Oracle, NetSuite, and Dynamics. No touching master data or audit trails.
[CTA Button] Explore AI for ERP
[H3] AI for CRM
[Body] Pipeline intelligence and account briefs from Salesforce, HubSpot, and Dynamics. No change to how reps work.
[CTA Button] Explore AI for CRM

[Section: services-platform-agnostic-heading]
[Eyebrow] Platform Agnostic
[H2] Our engagements run on
[Body] MES platforms we’ve worked with or modeled against
[Body] And any AI layer
[Body] The intelligence is in the methodology

[Section: services-legal-disclaimer]
[H3] Legal Disclaimer: Results & Outcomes
[Body] Prime AI provides consulting services and AI methodology. Client results depend on implementation, data quality, organizational adoption, and other factors outside Prime AI’s control. Past performance does not guarantee future results.
[Body] Prime AI does not guarantee specific business outcomes, yield improvements, decision speed increases, or other manufacturing results. Results described in case studies reflect the specific client’s situation, database architecture, and implementation approach.
[Body] AI Validation:
[Body] Data Access:
[Body] Timeline Qualification:

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Ai4 2026 · Las Vegas
[List item] Who we’re for
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /ai-mes  (ai-mes.html)

[Page title] AI for MES · Manufacturing Intelligence at the Speed of a Question
[Meta description] MES + AI integration. MES stays the system of record. AI removes every barrier between your data and your decisions. Platform agnostic. Works with Camstar, SAP ME, Siemens Opcenter, FactoryTalk, and custom MES.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] MES + AI Integration
[H1] Manufacturing intelligence at the speed of a question.
[Body] MES stays the system of record. AI removes every barrier between your data and your decisions.
[CTA Button] Book Discovery Call
[CTA Button] See Methodology

[Section: section]
[Body] Semiconductor and advanced manufacturing environments carry years of customizations, interfaces, reports, and integrations.
[Body] The data exists. The insight does not.
[Body] Engineers write SQL tickets. DBAs build reports. Managers wait three days for answers that should take three seconds.
[Body] We fix that. Without replacing your MES, without ripping out your infrastructure, and without a two-year implementation.

[Section: section]
[Eyebrow] Before / After
[H2] Today vs. with Prime AI.

[Section: section]
[Eyebrow] Three Horizons
[H2] What changes first.
[List item] Now
[H3] Short-term operational lift
[List item] Natural language queries against MES data (yield trends, WIP status, equipment downtime, cycle time) without SQL or developer tickets.
[List item] Faster reporting: what used to take days takes minutes. Same data. No new systems.
[List item] Accelerated root cause analysis: AI correlates excursions, rework, tooling, and history faster than manual investigation, with receipts.
[List item] Reduced IT backlog: engineers answer their own exploratory questions inside governed guardrails. Developers focus on architecture, not report tickets.
[List item] Next
[H3] Medium-term depth
[List item] AI-assisted MES development: faster prototyping of queries, APIs, and integrations with appropriate human review gates.
[List item] Cross-system intelligence: bridge ERP, SPC, quality, and supply chain where policy allows.
[List item] Conversational manufacturing analytics: “Why did yield step down on line three overnight?” Structured answers. Traceable evidence. Human validation required before action.
[List item] Scale
[H3] Long-term intelligence posture
[List item] Proactive operational signals alongside human authority. Predictive, not prescriptive.
[List item] Democratized MES data: broader conversational literacy across operations, engineering, and executive teams.
[List item] Multi-plant expansion: the same governed AI layer deployed across every facility.

[Section: platform-agnostic-heading]
[Eyebrow] Platform Agnostic
[H2] Our methodology works
[Body] MES platforms we’ve worked with or modeled against
[Body] And any AI layer
[Body] The intelligence is in the methodology

[Section: mes-methodology-bridge-heading]
[Eyebrow] Shared framework
[H2] The full 10-phase roadmap — manufacturing reference
[Body] This is where we go deepest: lot genealogy, yield, equipment downtime, SME validation on the shop floor. The methodology page documents every phase with MES-specific deliverables. ERP and CRM engagements follow the same sequence.
[CTA Button] See the full roadmap
[CTA Button] Start with Diagnostics

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /ai-erp  (ai-erp.html)

[Page title] AI for ERP · Governed Intelligence on Top of SAP, Oracle, NetSuite, Dynamics
[Meta description] ERP + AI integration. Your ERP stays the system of record. AI surfaces the insight your finance, ops, and supply chain teams need without ripping anything out.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] ERP + AI Integration
[H1] Your ERP holds the truth.
[Body] SAP, Oracle, NetSuite, Microsoft Dynamics. AI sits on top with governed access, without replacing the system of record.
[CTA Button] Book Discovery Call
[CTA Button] See Methodology

[Section: section]
[Body] ERP environments accumulate two decades of customizations, batch jobs, integrations, and policy. Finance trusts the numbers in the ERP. Almost no one asks the ERP a question.
[Body] Reports are scheduled. Custom queries are gatekept. Cross-module questions like “why did margin compress on this product family last quarter?” sit in a backlog waiting for a consultant.
[Body] We close that gap without touching your master data, your close process, or your audit trail.

[Section: section]
[Eyebrow] Before / After
[H2] Today vs. with Prime AI.

[Section: section]
[Eyebrow] Three Horizons
[H2] From first wins to enterprise scale.
[List item] Now
[H3] Short-term operational lift
[List item] Plain-English access to GL, AP, AR, inventory, sales orders, and purchase data without opening a BI ticket.
[List item] Faster month-end variance research: AI explains exceptions before the controller has to chase them.
[List item] Vendor and customer 360s assembled on demand from FI, MM, and SD modules.
[List item] Reduced report queue: routine questions answered in seconds with logged, auditable lineage.
[List item] Next
[H3] Medium-term depth
[List item] Cross-system intelligence: ERP joined with MES production data, CRM pipeline, and supply chain signals under one governance model.
[List item] AI-assisted analyst workflows: variance analysis, supplier risk scoring, working-capital diagnostics. Drafted by AI. Validated by humans.
[List item] Forecast diagnostics: AI traces forecast-actual deltas to source transactions, not just buckets.
[List item] Scale
[H3] Long-term intelligence posture
[List item] Continuous controls: AI surfaces SoD violations, GL anomalies, and unusual journal patterns continuously, not at audit time.
[List item] Multi-entity, multi-ledger reach: the same governed AI layer across every entity and accounting standard.
[List item] Conversational FP&A and operations literacy: the ERP becomes a system anyone in the company asks.

[Section: platform-agnostic-heading]
[Eyebrow] Platform Agnostic
[H2] Our methodology works
[Body] ERP platforms we’ve worked with or modeled against
[Body] And any AI layer
[Body] The intelligence is in the methodology

[Section: erp-methodology-bridge-heading]
[Eyebrow] Shared framework
[H2] Same 10 phases — applied to ERP & finance operations
[Body] Inventory the schema, map relationships and batch logic, build approved views, validate against close and FP&A reports. The methodology page walks through the sequence with a manufacturing reference; your deliverables follow the same governed path.
[CTA Button] See the full roadmap
[CTA Button] Start with Diagnostics

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /ai-crm  (ai-crm.html)

[Page title] AI for CRM · Pipeline Intelligence for Salesforce, HubSpot, Dynamics
[Meta description] CRM + AI integration. Your reps stop fighting the CRM. AI surfaces the pipeline signals, account intelligence, and forecast diagnostics your team should already have.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] CRM + AI Integration
[H1] Your CRM is full of signal.
[Body] Salesforce, HubSpot, Dynamics. AI surfaces account context, pipeline movement, and forecast risk in plain English.
[CTA Button] Book Discovery Call
[CTA Button] See Methodology

[Section: section]
[Body] CRMs collect everything and surface almost nothing. The data is rich. The intelligence is missing.
[Body] Reps spend hours in dashboards instead of accounts. Managers chase pipeline updates that should answer themselves. Leaders rely on forecasts assembled from gut feel and aging fields.
[Body] We turn your CRM into a system that answers questions. Your team keeps entering data exactly as they do today.

[Section: section]
[Eyebrow] Before / After
[H2] Today.

[Section: section]
[Eyebrow] Three Horizons
[H2] From rep enablement to revenue intelligence.
[List item] Now
[H3] Short-term operational lift
[List item] Account briefs generated on demand from CRM, calls, emails, and product usage signals.
[List item] Pipeline questions answered conversationally: no report builder, no spreadsheet.
[List item] Stalled opportunity flagging with the actual reason from notes and activity history.
[List item] CRM hygiene assistance: AI suggests fields to update, never overwrites without rep confirmation.
[List item] Next
[H3] Medium-term depth
[List item] Cross-system intelligence: CRM joined with ERP order data, support tickets, and product usage, all in the same governed semantic layer.
[List item] Forecast diagnostics: AI explains gaps between commit and pipeline at the deal level, with evidence.
[List item] Manager 1:1 prep: AI assembles rep-specific coaching context from activity, win/loss, and stage progression.
[List item] Scale
[H3] Long-term intelligence posture
[List item] Revenue intelligence as a daily habit: leadership asks the CRM directly, with auditable answers.
[List item] Customer 360 across the entire stack: marketing, sales, success, support, and product under one access policy.
[List item] Multi-region, multi-segment expansion of the same governed AI surface.

[Section: platform-agnostic-heading]
[Eyebrow] Platform Agnostic
[H2] Our methodology works
[Body] CRM platforms we’ve worked with or modeled against
[Body] And any AI layer
[Body] The intelligence is in the methodology

[Section: crm-methodology-bridge-heading]
[Eyebrow] Shared framework
[H2] Same 10 phases — applied to CRM & revenue operations
[Body] Map objects and integrations, document how pipeline logic actually works, build governed views for revenue questions, validate with sales and success SMEs. The methodology page uses MES as the worked example — the phase structure is identical for CRM.
[CTA Button] See the full roadmap
[CTA Button] Start with Diagnostics

[Section: Next steps]

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /company  (company.html)

[Page title] About · Prime AI Consultants
[Meta description] Founder-led boutique: governed AI on operational data. 30+ years enterprise systems, deepest in manufacturing — same playbook for ERP and custom apps.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] About Prime AI
[H1] Governed AI on operational data — built by people who’ve run the systems.
[Body] The methodology wasn’t developed in a consulting office. It was developed inside real manufacturing operations — and applies wherever legacy databases block trusted AI.

[Section: section]
[Body] The Founder
[Body] The company was founded by someone with 30 years of enterprise systems experience and 18 years specifically inside semiconductor and discrete manufacturing operations.
[Body] That background informs every decision we make:
[List item] We know why MES databases are structured the way they are
[List item] We understand the business logic hidden in stored procedures
[List item] We know what “trusted source” means in manufacturing
[List item] We’ve solved these problems before, for real clients, with real data
[List item] We don’t theorize about manufacturing—we’ve lived it

[Section: section]
[Eyebrow] What We Believe
[Body] Operational AI projects fail not because of the model. They fail because nobody mapped the database before plugging in AI.
[Body] Antonio spent 18 years inside manufacturing operations. That’s our deepest credibility — and the same governed playbook works for ERP, healthcare ops, and financial data.
[Body] Our mission: build the AI intelligence layer that manufacturing has been waiting for. Governed by design. Trusted by operations teams. Built to stay in production.

[Section: section]
[Eyebrow] How We Work
[H2] Four operating principles
[Body] We never connect AI directly to raw MES tables. Every AI connection goes through a governed semantic layer. Read-only. Logged. Auditable.
[Body] The methodology is proven against real manufacturing data, not whitepapers. We don’t guess about manufacturing. We know.
[Body] When the engagement ends, you own the code, documentation, data dictionary, and semantic layer. There is no vendor lock-in.
[Body] If the audit reveals the problem is upstream of AI (process, data quality, organizational alignment), we report it clearly. We’re not here to confirm your existing plan. We’re here to give you the truth.

[Section: section]
[Eyebrow] Why Choose Prime AI
[H2] You’ve been burned before.
[Body] You’ve probably worked with consultants who connected AI to your MES and produced answers nobody trusted. Or who understood AI but not manufacturing. Or who built something that required them to stay involved forever.
[List item] 30 years of enterprise systems experience
[List item] 18 years inside manufacturing operations
[List item] Methodology built inside real production environments
[List item] Working infrastructure delivered, not demos or slide decks
[List item] You own what we build. No lock-in. No subscription required.

[Section: team]
[Eyebrow] The Team
[H2] The people who built the methodology.
[H3] Antonio Rojas
[Body] 30 years of enterprise systems experience, including 18 years inside semiconductor and discrete manufacturing operations. Not as a consultant visiting facilities. As someone who built, debugged, and improved production systems.
[Body] He knows where yield data hides, why reports break under pressure, and what engineers will actually trust when the logic is transparent.
[Body] Before Prime AI, he led applications development and SAP implementations across North America and Latin America in enterprise manufacturing environments.
[Body] Every engagement starts with understanding your specific system, constraints, and definition of truth before any AI connection is made.
[H3] Fernando Rojas
[Body] Fernando builds the infrastructure that turns manufacturing expertise into a scalable business. His background spans product, engineering, and how those two things should actually talk to each other. He earned a Bachelor of Science in Web Design and Engineering from Santa Clara University and is pursuing a Master’s in Computer Science through Harvard Extension School.
[Body] Most recently, he built enterprise career platforms at Disney—the systems and candidate experiences that run global talent acquisition for one of the world’s largest companies. Before that: product-scale work at La Mer (Estée Lauder), technical implementation at Santa Clara University, and AR experiences at Snap.
[Body] At Prime AI, he turns deep operations expertise into repeatable, governed delivery—so what Antonio knows from 30 years in the field becomes infrastructure teams can actually use.
[Body] He’s comfortable in three domains: building technical systems that work, understanding product-market fit, and doing the unglamorous work of turning expertise into scalable processes.

[Section: section]
[Eyebrow] Get in Touch
[H2] Ready to build AI infrastructure
[Body] Schedule a 30-minute discovery call. No sales pitch. No pressure. We typically respond within 24 hours.
[CTA Button] Book Discovery Call
[CTA Button] Email Us
[Body] hello@primeaiconsultants.com · (805) 216-4651

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Ai4 2026 · Las Vegas
[List item] Who we’re for
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.
[Sticky CTA] Book Discovery Call


### Page: /contact  (contact.html)

[Page title] Contact · Book Your Free Discovery Call
[Meta description] Book a free 30-minute discovery call. Honest assessment of your operational data, AI readiness, and timeline. Meeting at Ai4 Aug 4–6, Las Vegas.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] Contact
[H1] Ready to build AI infrastructure your team trusts?
[Body] If your AI pilot stalled on messy operational data — MES, ERP, or custom apps — start with a conversation. We map what you have, build governed access, and deliver infrastructure your SMEs can defend.
[Body] Attending Ai4
[Body] See who we’re built for

[Section: schedule]
[H2] Schedule a discovery call
[Label] First Name*
[Label] Last Name*
[Label] Company*
[Label] Job Title*
[Label] Email*
[Label] Phone
[Label] Primary operational system
[Option] Select system (optional)
[Option] Camstar
[Option] SAP ME / MII
[Option] Siemens Opcenter
[Option] FactoryTalk
[Option] Oracle MES
[Option] SAP ECC / S/4
[Option] Oracle ERP
[Option] Microsoft Dynamics
[Option] NetSuite
[Option] Custom operational database
[Option] CRM / revenue ops (Salesforce, etc.)
[Option] Multiple systems
[Option] Not sure yet
[Label] Timeline (Optional)
[Option] Select timeline
[Option] Immediate (next 30 days)
[Option] Near-term (60–90 days)
[Option] Planning phase (6+ months)
[Option] Just exploring
[Label] Message*
[Placeholder] Tell us about your systems (MES, ERP, etc.), data challenges, and whether you are attending Ai4.
[Button] Schedule Your Discovery Call
[Body] We’ll ask about your operational systems, data challenges, and what success looks like. No sales pitch. No pressure.
[H3] The Typical Engagement
[List item] Weeks 1–2 (Prime Diagnostics):
[List item] Weeks 3–12 (Prime Build):
[H3] Next Steps
[List item] Schedule a 30-minute discovery call.
[List item] If it makes sense, we propose Prime Diagnostics.
[List item] Then you decide.
[H3] Are we a fit?
[Body] Yes
[Body] Maybe
[Body] Probably not
[List item] MES / Camstar
[List item] SAP ME / ERP
[List item] Oracle
[List item] Siemens Opcenter
[List item] Custom ops DBs
[Body] Shop floors, finance ops, healthcare operations, revenue intelligence.
[H3] Contact
[List item] hello@primeaiconsultants.com
[List item] (805) 216-4651
[List item] Los Angeles, CA
[List item] We typically respond within 24 hours.

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] (805) 216-4651
[List item] Los Angeles, CA
[List item] Ai4 2026 · Las Vegas
[List item] Who we’re for
[List item] Schedule a Call
[Body] The next AI revolution is in the physical world.


### Page: /privacy  (privacy.html)

[Page title] Privacy Policy · Prime AI Consultants
[Meta description] Prime AI Consultants Privacy Policy. How we collect, use, store, and protect information from website visitors and clients.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] Legal
[H1] Privacy Policy
[Body] How Prime AI Consultants LLC collects, uses, stores, and protects your information.

[Section: section]
[Body] Effective Date: May 9, 2026 · Last Updated: May 9, 2026
[Body] This Privacy Policy describes how Prime AI Consultants LLC (“Prime AI,” “we,” “us,” or “our”) collects, uses, and discloses information about you when you visit our website at primeaiconsultants.com (the “Site”) or engage with us through forms, email, or scheduled calls.
[H2] 1. Information We Collect
[H3] Information you provide directly
[Body] When you submit a discovery call request, contact us by email, or otherwise communicate with us, you may provide:
[List item] Name, email address, and phone number
[List item] Company name, job title, and industry
[List item] Information about your MES, ERP, CRM, or other enterprise environment
[List item] Any other content you choose to include in your message
[H3] Information collected automatically
[Body] Like most websites, we collect limited technical information from your browser, including IP address, browser type, device type, referring URL, pages viewed, and timestamps. This information is used solely for site analytics and security.
[H2] 2. How We Use Information
[Body] We use the information you provide to:
[List item] Respond to inquiries and schedule discovery calls
[List item] Deliver services to clients we have engaged with
[List item] Send relevant operational communications (no marketing email lists)
[List item] Improve our website and content
[List item] Comply with legal obligations
[Body] We do not sell, rent, or trade personal information to third parties.
[H2] 3. Sharing of Information
[Body] We share information only with:
[List item] Service providers
[List item] Legal authorities
[List item] Successors
[H2] 4. Client Data & Confidentiality
[Body] For client engagements, we operate under written confidentiality terms (NDA, MSA, or equivalent). Production data accessed during an engagement is read-only by default, logged, and used solely for the agreed scope of work. Data is not retained beyond the engagement except where required by contract or law.
[H2] 5. Cookies & Analytics
[Body] The Site may use cookies and similar technologies for essential functionality and aggregated analytics. You can disable cookies in your browser; some site features may not function as expected.
[H2] 6. Data Retention
[Body] Inquiry information is retained for the period necessary to respond and follow up, typically up to 24 months, unless a longer period is required by contract or law. Client engagement records are retained per the applicable engagement terms.
[H2] 7. Security
[Body] We use reasonable administrative, technical, and physical safeguards to protect information. No method of transmission or storage is 100% secure, but our security posture documentation is available to clients on request.
[H2] 8. Your Rights
[Body] Depending on your jurisdiction, you may have the right to access, correct, delete, or restrict use of your personal information. To exercise these rights, contact us at hello@primeaiconsultants.com
[H2] 9. International Visitors
[Body] The Site is operated from the United States. If you visit from outside the U.S., information collected will be transferred to and processed in the U.S.
[H2] 10. Changes to This Policy
[Body] We may update this Privacy Policy from time to time. The “Last Updated” date at the top reflects the most recent revision. Material changes will be highlighted on the Site.
[H2] 11. Contact Us
[Body] Questions about this Privacy Policy or our data practices:
[Body] Prime AI Consultants LLC
[Body] This document is a starter Privacy Policy provided as a placeholder. For binding legal protection, replace with a final policy reviewed by qualified counsel or generated through a service such as Termly or Iubenda.

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[List item] Ai4 2026 · Las Vegas
[Sticky CTA] Book Discovery Call


### Page: /terms  (terms.html)

[Page title] Terms of Service · Prime AI Consultants
[Meta description] Prime AI Consultants Terms of Service. The terms governing use of primeaiconsultants.com and any informational content we publish.

[Section: Global: Ai4 Toast]
[Body] Meet Prime AI
[CTA Button] Book a meeting

[Section: Global: Navigation]
[List item] Home
[List item] Methodology
[List item] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[List item] Solutions
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[List item] About
[List item] Contact
[CTA Button] Book Discovery Call
[CTA Button] Book Discovery Call

[Section: section]
[Eyebrow] Legal
[H1] Terms of Service
[Body] The terms governing use of primeaiconsultants.com.

[Section: section]
[Body] Effective Date: May 9, 2026 · Last Updated: May 9, 2026
[Body] These Terms of Service (“Terms”) govern your access to and use of primeaiconsultants.com (the “Site”), operated by Prime AI Consultants LLC (“Prime AI,” “we,” “us,” or “our”). By using the Site, you agree to these Terms. If you do not agree, do not use the Site.
[H2] 1. Use of the Site
[Body] The Site is provided for informational purposes about Prime AI’s services. You may use the Site for lawful, non-commercial review of our content. You agree not to:
[List item] Use the Site to violate any applicable law or regulation.
[List item] Attempt to gain unauthorized access to any portion of the Site or related systems.
[List item] Interfere with or disrupt the Site, including by introducing malicious code.
[List item] Scrape, copy, or republish content for commercial purposes without written permission.
[H2] 2. Engagement Terms (Separate)
[Body] Any consulting, advisory, or implementation services Prime AI provides are governed by a separately executed agreement (such as a Master Services Agreement, Statement of Work, or NDA). These Terms do not create a consulting relationship. The Site itself does not constitute an offer of services.
[H2] 3. Intellectual Property
[Body] All content on the Site, including text, graphics, logos, methodology descriptions, and visual design, is owned by Prime AI Consultants LLC or used under license, and is protected by U.S. and international copyright and trademark law. The Prime AI methodology, frameworks, and naming conventions are the intellectual property of Prime AI Consultants LLC.
[H2] 4. Discovery Calls
[Body] Discovery calls are complimentary and informational. Information shared during a discovery call is held confidentially per our standard practice. A discovery call does not create a contractual obligation on either party. Engagements begin only after a written agreement is signed.
[H2] 5. No Warranty
[Body] The Site and its content are provided “as is” and “as available,” without warranties of any kind, express or implied, including warranties of merchantability, fitness for a particular purpose, or non-infringement. While we work to keep information accurate and current, we do not warrant that the Site will be uninterrupted, error-free, or free from harmful components.
[H2] 6. Limitation of Liability
[Body] To the maximum extent permitted by law, Prime AI Consultants LLC will not be liable for any indirect, incidental, special, consequential, or punitive damages arising out of or related to your use of the Site, even if advised of the possibility of such damages. Our total aggregate liability arising out of or related to the Site shall not exceed one hundred U.S. dollars ($100).
[H2] 7. Indemnification
[Body] You agree to indemnify and hold harmless Prime AI Consultants LLC and its members, employees, and contractors from any claims, damages, losses, or expenses arising from your misuse of the Site or violation of these Terms.
[H2] 8. Third-Party Links
[Body] The Site may include links to third-party websites or services. Prime AI does not control and is not responsible for the content, policies, or practices of those third parties.
[H2] 9. Modifications
[Body] We may update these Terms from time to time. Material changes will be reflected by an updated “Last Updated” date. Continued use of the Site after changes constitutes acceptance of the updated Terms.
[H2] 10. Governing Law
[Body] These Terms are governed by the laws of the State of California, without regard to conflict-of-laws principles. Venue will lie in the state or federal courts located in California, subject to applicable law.
[H2] 11. Contact
[Body] Questions about these Terms:
[Body] Prime AI Consultants LLC
[Body] This document is a starter Terms of Service provided as a placeholder. For binding legal protection, replace with final terms reviewed by qualified counsel or generated through a service such as Termly or Iubenda.

[Section: Footer]
[Body] Governed AI on operational data you already run. Deepest in manufacturing — built for any team stalled on legacy MES, ERP, or custom apps.
[H2] Services
[List item] All Services
[List item] Prime Diagnostics
[List item] Prime Build
[List item] Prime Retainer
[H2] Methodology
[List item] 10-Phase Roadmap
[List item] AI for MES
[List item] AI for ERP
[List item] AI for CRM
[H2] Connect
[List item] hello@primeaiconsultants.com
[List item] Antonio Rojas: (805) 216-4651
[List item] Los Angeles, CA
[List item] Schedule a Call
[List item] Ai4 2026 · Las Vegas
[Sticky CTA] Book Discovery Call


---

## Section 3 — Styling & Design Tokens

### Architecture
- **Centralized:** CSS custom properties in `assets/styles.css` (`:root` block, lines 9–91)
- **Extensions:** `assets/enhancements.css` adds glass effects, homepage widgets, Ai4 toast, industry dial, proof cards, tablet hero overrides, methodology bridges (~3,500 lines)
- **No Tailwind, no CSS-in-JS, no theme JSON**
- **Inline styles:** 4 instances only (`contact.html` ×2, `company.html` ×2, `services.html` ×1) — all `commercial-note` / lede spacing
- **Fonts loaded via Google Fonts** in each HTML `<head>`: Manrope, Source Sans 3, Fraunces (italic accent on homepage hero desktop)

### Color tokens (`:root` in styles.css)
| Token | Hex / value | Usage |
|-------|-------------|-------|
| `--color-dark` | `#0A0F1E` | Primary dark backgrounds (hero, nav, footer) |
| `--color-dark-2` | `#0D1428` | Hero gradient secondary |
| `--color-navy` | `#0D1B3E` | Accent dark / brand |
| `--color-teal` | `#00D4B8` | Primary CTA, eyebrows on dark, links on dark |
| `--color-teal-dark` | `#00A896` | Button hover, accents |
| `--color-teal-text-on-light` | `#0d7d72` | Teal text on white/mist (AA) |
| `--color-teal-outcome` | `#009b89` | Outcome blocks |
| `--color-teal-soft` | `rgba(0, 212, 184, 0.12)` | Soft teal fills |
| `--color-white` | `#FFFFFF` | Cards, light sections |
| `--color-off-white` | `#F8F8F6` | Alternate light bg |
| `--color-light-grey` | `#F0F0F0` | Legacy light grey |
| `--color-mist` | `#F5F5F7` | Section-mist backgrounds |
| `--color-mid-grey` | `#8A8A9A` | Muted UI |
| `--color-text-muted-on-light` | `#5a5a6e` | Secondary text on light |
| `--color-text-dark` | `#1A1A2E` | Body default on light |
| `--color-text-body` | `#4A4A5A` | Lede / secondary body |
| `--color-border` | `#E0E0E8` | Light borders |
| `--color-border-dark` | `rgba(255,255,255,0.12)` | Dark surface borders |

### Additional colors in enhancements.css (not in :root)
- `#0a4a7e`, `#0a0f1e`, `#2a2a3e`, `#5a5a7e`, `#5a6478`, `#141d33`, `#e8e8ed`, `#f0f4f8`, `#f4f5f8`, `#f9f9fb` — roadmap phase cards, methodology panels, proof rails
- Phase accent colors on roadmap cards: `#2c4f8c`, `#0f9b8f`, `#059669`, `#ca8a04`, `#ea580c`, `#db2777`, `#7c3aed`, `#1e3a5f`, `#1e293b`
- `--gradient-brand`: `linear-gradient(135deg, #00D4B8 0%, #00A896 48%, #0D7D72 100%)`
- Glass tokens: `--glass-bg`, `--glass-border`, `--glass-blur`

### Typography
| Role | Font | Size | Weight | Notes |
|------|------|------|--------|-------|
| H1 hero (`.h-hero`) | Manrope (`--font-display`) | `--text-hero`: clamp(32–48px mobile; 48–96px ≥921px) | 600 | Homepage hero only |
| H1 page (`.h-h1`) | Manrope | `--text-h1`: clamp(36–64px) | 600 | Interior page heroes |
| H2 (`.h-h2`) | Manrope | clamp(28–44px) | 600 | Section headings |
| H3 (`.h-h3`) | Manrope | 24px (`--text-h3`) | 600 | Cards, phase names |
| Body | Source Sans 3 (`--font-body`) | 16px (`--text-body`) | 400 | Default |
| Lede | Source Sans 3 | 20px (`--text-body-lg`) | 400 | `.lede`, `.hero-sub` |
| Eyebrow | Source Sans 3 | 16px default; 32px desktop hero; mono on some sections | 700 | Uppercase + `[ ]` pseudo brackets except home hero variants |
| Captions / small | Source Sans 3 / mono | 12–14px | 400–600 | `.text-mono`, roadmap hints, pills |
| Hero accent line | Fraunces italic (`--font-serif-accent`) | inherits H1 | 500 | Desktop only: last line of homepage H1 |
| Buttons | Source Sans 3 | 15px default; 14px sm; 16px lg | 600 | `.btn` family |

### Button variants
| Class | Padding | Radius | Background | Text | Border |
|-------|---------|--------|------------|------|--------|
| `.btn` (base) | 14px 28px | 6px (`--radius-sm`) | — | — | 1.5px transparent |
| `.btn-sm` | 10px 20px | 6px | inherits | 14px | — |
| `.btn-lg` | 18px 36px | 6px | inherits | 16px | — |
| `.btn-primary` | — | — | `#00D4B8` → hover `#00A896` | `#0A0F1E` | teal |
| `.btn-secondary` | — | — | transparent | white | `rgba(255,255,255,0.4)` |
| `.btn-secondary-light` | — | — | transparent | `#0A0F1E` | `rgba(10,15,30,0.25)` |
| `.btn-link` | — | — | none | `#0d7d72` on light / `#00D4B8` on dark | underline |
| `.dual-panel` | large tap targets | 0 | light `#F5F5F7` or dark `#0A0F1E` | — | — |
| `.sticky-cta` | fixed pill | 999px | teal gradient | dark text | — |

### Spacing & layout
- Container max-width: `1240px` (`--max-width`)
- Text max-width: `720px` (`--max-width-text`), narrow `560px`
- Section padding: `clamp(72px, 10vw, 128px)` vertical (`--section-pad`)
- Horizontal padding: `clamp(20px, 5vw, 48px)` (`--content-pad-x`)
- Nav height: `72px` mobile → `clamp(108px, 13vh, 148px)` desktop
- Breakpoints: `921px` (desktop nav), `768–920px` (tablet homepage centering), `767px` (mobile site-wide), `480px` (small phone)

### Inconsistencies observed
1. **Eyebrow brackets:** Global `.eyebrow::before/after` adds `[ ]`; homepage mobile uses custom stacked brackets; tablet/desktop use different eyebrow variants — three systems.
2. **Hard-coded hex in enhancements.css** alongside CSS variables — roadmap/methodology panels use `#5a5a7e` while tokens use `#5a5a6e` for muted text.
3. **H1 classes:** Homepage uses `.h-hero`; interior pages use `.h-h1` — different scale tokens.
4. **Commercial notes:** Three pages use inline `style=` on `.commercial-note` instead of a shared modifier class.
5. **CTA label drift:** `Book Discovery Call` vs `Book Free Discovery Call` vs `Book free discovery call` vs `Book a meeting` (Ai4 toast) — same intent, four phrasings.
6. **Footer tagline differs** on `index.html` vs interior pages (manufacturing emphasis vs generic ops).
7. **Legacy build script** (`scripts/render_pages.py`) references old fonts (Inter, Cormorant) — not used by live HTML.
8. **`page_content/*.frag.html`** fragments exist but live pages are hand-maintained full HTML files — dual content pipeline risk.

---

## Section 4 — Component Architecture Analysis

### 1. Framework and structure
- **Stack:** Static site — plain HTML5, CSS3, vanilla JavaScript (`assets/site.js`). No React/Vue/Svelte, no bundler, no SSG at build time for production (files served as-is).
- **Hosting:** Vercel static deploy; `vercel.json` for clean URLs, redirects, cache headers.
- **Assets:** SVG logos/visuals in `assets/`, optional hero video in `assets/hero/`.
- **Forms:** Formspree POST from `contact.html` (ID configured in `site.js`).
- **Legacy tooling:** `scripts/render_pages.py` + `page_content/*.frag.html` appear to be an older generation path; **live pages are monolithic HTML files** with duplicated nav/footer.

### 2. Reusable component architecture?
**No formal component system.** Each page is a large standalone `.html` file. Patterns are repeated via copy-paste markup and shared CSS class names — not includes, partials, or web components.

### 3. Existing reusable patterns (CSS + JS, not HTML components)
- **`.site-nav` + `.nav-inner`** — All 10 live pages (identical nav block duplicated)
- **`.footer` + `.footer-top`** — All 10 live pages
- **`.ai4-toast`** — Sitewide promotional toast
- **`.sticky-cta`** — Sitewide fixed CTA pill
- **`.home-shell` / `.home-shell--pad`** — Homepage + interior enhanced sections
- **`.section` + `.section-head` + `.eyebrow`** — Most content sections
- **`.dual-cta-section` + `.dual-panel`** — methodology, services, ai-mes, ai-erp, ai-crm
- **`.roadmap-native` widget** — index.html + methodology.html (large duplicated phase markup)
- **`.phase-detail--accordion`** — methodology.html only
- **`.engage-card`** — index.html + services.html
- **`.before-after-grid`** — ai-mes, ai-erp, ai-crm
- **`.platform-lattice`** — index.html + services + ai-* pages
- **`.reveal` / `.reveal-stagger`** — Sitewide scroll animation hooks in site.js

### 4. Duplicated markup (same pattern, raw HTML repeated)
- Full `<nav>` block (~30 lines) × 10 files
- Full `<footer>` block (~45 lines) × 10 files
- Ai4 toast `<aside>` × 10 files
- Sticky CTA anchor × 10 files
- Team member cards: `index.html` + `company.html` (near-duplicate bios)
- Platform lattice (MES/ERP/CRM logos grid) × 5 pages
- Before/After comparison grid × 3 ai-* pages
- Three Horizons cards × 3 ai-* pages
- Methodology bridge panel × 3 ai-* pages
- 10-phase roadmap horizontal cards: `index.html` (preview) + `methodology.html` (full) — largest duplication
- Engagement cards (Diagnostics/Build/Retainer): `index.html` + `services.html`
- Dual CTA pair at page bottom × 5 pages

### 5. Proposed widget-based component map

#### `SiteChrome`
- **Visual:** skip link, ai4 toast, nav, sticky CTA, footer
- **Props:** `activeRoute`, `showAi4Toast`, `footerTaglineVariant`
- **Pages:** All pages

#### `HeroSection`
- **Visual:** Dark hero with eyebrow, H1, lede, proof line, CTA row, optional video bg
- **Props:** `variant` (home | page), `eyebrow`, `headline`, `subcopy[]`, `ctas[]`, `scrollHint`, `systemPills[]`
- **Pages:** index, methodology, services, ai-*, company, contact

#### `TrustStrip`
- **Props:** `items[{icon, label}]`
- **Pages:** index

#### `CredibilityBar`
- **Props:** `stats[{value, label}]`, `footnote`
- **Pages:** index

#### `Ai4ConferenceBlock`
- **Props:** `badge`, `title`, `body`, `meta[]`, `ctas[]`, `pitch`
- **Pages:** index

#### `IndustryDial`
- **Props:** `tabs[{id, label, title, body, cta}]`
- **Pages:** index

#### `OutcomeCards` / `CapabilityGrid` / `ArchitectureDiagram` / `ProcessTimeline` / `StatsBar`
- **Pages:** index (homepage middle sections)

#### `ProblemSection` / `OperatorStory` / `DifferentiatorCards` / `ComparisonTable`
- **Pages:** index

#### `EngagementCards`
- **Props:** `cards[{name, phase, body, bullets, cta}]`
- **Pages:** index, services

#### `ProofCaseStudies` / `DataDictionaryPreview`
- **Pages:** index

#### `RoadmapPreview` + `PhaseAccordion`
- **Props:** shared `phases[]` data; `variant` compact | full
- **Pages:** index (preview), methodology (full + accordion)

#### `FrameworkApplies`
- **Pages:** methodology

#### `PlatformLattice` / `BeforeAfterGrid` / `HorizonsCards` / `MethodologyBridge`
- **Pages:** services, ai-* (shared vertical template)

#### `TeamSection`
- **Pages:** index, company

#### `IcpFitGrid` / `FaqAccordion` / `LeadMagnetCta` / `ClosingCta`
- **Pages:** index

#### `DualCtaBanner`
- **Pages:** methodology, services, ai-*

#### `ContactForm`
- **Pages:** contact

#### `LegalProse` / `ComplianceDisclaimer`
- **Pages:** privacy, terms, services, methodology

### 6. Migration estimate & risks

**Scope if migrating to composable components (e.g. Eleventy/Nunjucks, Astro, or React SSG):**
- **~10 page templates** + **~30 section partials** + **1 shared layout**
- **~2,500–4,000 lines** of HTML markup consolidation (nav/footer/toast alone ≈ 850 duplicated lines)
- **Largest win:** single `phases.json` feeding roadmap preview + methodology page + phase accordion
- **CSS:** mostly reusable as-is; optional split into per-component modules

| Risk | Severity | Mitigation |
|------|----------|------------|
| SEO meta / OG tags per page | High | Per-page frontmatter in SSG; preserve exact titles/descriptions |
| `vercel.json` clean URLs | Medium | Keep extensionless routes; test all redirects |
| Formspree + field names | High | Do not rename `name` attributes; keep hidden fields |
| Active nav / hash routing (`#diagnostics`) | Medium | Port `setActiveNav()` logic; test Services dropdown |
| Ai4 toast localStorage dismiss | Low | Preserve `initAi4Toast()` behavior |
| Scroll reveal animations | Low | `site.js` selectors must match post-migration class names |
| Duplicate content drift during migration | High | Migrate one page at a time; diff against this audit |
| Analytics / third-party scripts | Low | None currently embedded beyond Formspree |

**Recommended migration order:** Layout chrome → interior pages (company, contact) → services → methodology (roadmap data) → homepage (most sections) → ai-* verticals (share 80% structure).
