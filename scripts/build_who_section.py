# One-off generator: merges WHO WE SERVE section HTML into ../index.html
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
MARKER = "<!-- ============== WHY CHOOSE US ============== -->"


def esc(s):
    return html.escape(s, quote=False)


# Order = tab order: Local & growing businesses → Manufacturers → Individuals (default Local first)
DATA = [
    {
        "id": "local",
        "label": "Local & growing",
        "title_attr": esc(
            "For plumbing, contracting, consulting, clinics, and shops—we start with a free website mockup and grow from there."
        ),
        "accent": "#1F8A5B",
        "eyebrow": "For local & growing businesses",
        "headline": "Your business runs on you.",
        "headline_em": "That's the problem.",
        "lede": "You're great at your work—plumbing, contracting, consulting, whatever it is. But you're also scheduling, invoicing, chasing payments, and answering the same questions over and over. The work that pays you isn't getting done because the work that processes payment is.\n\nWe start by building you a real website with an online booking system. While we build it, we learn how your business actually works. We notice what's killing your time. Then we fix it.",
        "cards": [
            {
                "glyph": "qf",
                "practice_heading": "WHAT WE DELIVER",
                "title": "A website that actually captures customers.",
                "intro": "Right now, customers search for your service, find a competitor with a working website and a \"Book now\" button, and you never get the call.",
                "problem": "",
                "solution": "We build you a real, working website with an online booking calendar. It captures customers 24/7, even when you can't pick up the phone.",
                "why": "A real website is the single biggest revenue lever for a local business. It looks like you're a serious operation. It turns a casual searcher into a booked job. It works while you sleep.",
                "examples": [
                    "Five-page site (services, about, reviews, booking, contact)",
                    "Live booking calendar synced to your phone/email",
                    "Local SEO basics so you actually appear on Google Maps",
                    "All copy written for your actual business",
                    "Mobile-optimized so customers can book from their phone",
                ],
            },
            {
                "glyph": "star",
                "practice_heading": "WHAT WE BUILD",
                "title": "Three hours a week on billing.",
                "intro": "That's 150 hours a year you're not working. You finish a job, you send an invoice manually, you chase payment manually. It's tedious and it's not the work you started this business to do.",
                "problem": "Manual billing steals time you could spend on paid work.",
                "solution": "We design a workflow that drafts invoices from your job notes, sends payment reminders in your voice on a schedule, and flags unpaid invoices so they don't slip. You review once, it runs forever.",
                "why": "Every hour you spend on billing is an hour you're not on a job site earning money. Automation gives you that time back. It also removes the awkwardness of chasing payment—the reminder is automatic and consistent.",
                "examples": [
                    "Auto-drafted invoices (from your job notes or voice memos)",
                    "Payment reminders sent automatically, in your voice",
                    "Unpaid invoice alerts (so nothing falls through the cracks)",
                    "Integration with your booking system (one source of truth)",
                ],
            },
            {
                "glyph": "flower",
                "practice_heading": "WHAT WE BUILD",
                "title": "Half your customers would leave a five-star review if you asked.",
                "intro": "You don't ask.",
                "problem": "You finish the job, you move to the next one, and the review never happens. Your competitor has fifty reviews. You have eight. Local SEO favors them.",
                "solution": "We build a simple follow-up sequence, text and email, tied to your invoice system. It asks for the review at the right moment, in your voice, with a direct link. You never have to think about it.",
                "why": "Reviews compound. The more you have, the more local search trusts you, the more leads you get, the more reviews you accumulate. Skipping the follow-up is the single biggest unforced error a local business makes.",
                "examples": [
                    "Post-job follow-up (text or email, your choice)",
                    "Thank-you message in your voice and tone",
                    "One-tap review link (takes 10 seconds for the customer)",
                    "Alert when a new review lands",
                    "Quarterly digest of all reviews",
                ],
            },
        ],
        "process_eyebrow": "Together",
        "process_headline": "How we work together",
        "process_subline": "",
        "process": [
            (
                "WEEK 1: DISCOVERY CALL",
                "You tell us about your business. We ask specific questions: How do you book jobs? How do you invoice? Who's your ideal customer? What's broken?",
            ),
            (
                "WEEK 2–4: FREE MOCKUP",
                "We build a working website mockup with your branding, your services, your actual copy. You can click through every page. You see exactly what you're getting. Zero commitment.",
            ),
            (
                "WEEK 5+: BUILD & DISCOVER",
                "If you like the mockup, we start building the real thing. As we build, we notice patterns. \"Your invoicing is manual.\" \"You're chasing payment constantly.\" \"You never ask for reviews.\" We propose automations that actually matter.",
            ),
            (
                "ONGOING: YOU OWN IT",
                "The website is yours. The code is yours. Any automation we build is yours. You can edit it, extend it, or hand it off to someone else. No retainer. No vendor lock-in.",
            ),
        ],
        "stats": [
            ("Free mockup first", "See work before you commit"),
            ("Custom quotes", "Transparent scope and price"),
            ("You own it", "Site, flows, code stay yours"),
        ],
        "pricing": [
            (
                "Free mockup · custom quote for build",
                "The mockup is free and takes 2–4 weeks depending on your project scope. We'll tell you upfront what it includes and when you'll see it.\n\n"
                "Once you approve the mockup, we quote the full build. Price varies based on complexity, integrations, and the automations you want to add. "
                "Most local businesses spend $3–8K for website + one automation. Some spend more. Some spend less. "
                "We'll be transparent about the cost and timeline before you commit to anything.",
            )
        ],
    },
    {
        "id": "enterprise",
        "label": "Manufacturers",
        "title_attr": esc(
            "MES, ERP, yield diagnostics, and supply-chain visibility—read-only connectors and plain-English answers."
        ),
        "accent": "#0052CC",
        "eyebrow": "For manufacturers",
        "headline": "Your data holds every answer.",
        "headline_em": "Nobody can read it.",
        "lede": "Manufacturing data lives in MES tables. Supply chain data lives in ERP. Quality data lives in SPC. The problem is the same: nobody outside the original implementation team can read it.\n\n"
        "Your engineers know something is wrong on Tool 7. Proving it takes a week of SQL and a post-mortem. Your planners can't ask \"why are we out of stock?\" in plain language. "
        "Your yield is bleeding money and you're hunting for the cause instead of fixing it.\n\n"
        "We embed AI directly into the systems where work already happens. Your team asks a question in plain English and gets an answer with citations. No data science required.",
        "cards": [
            {
                "glyph": "qf",
                "practice_heading": "WHAT WE DELIVER",
                "title": "Your MES is producing data faster than humans can read it.",
                "intro": "Twenty percent of your production data lives in tables that only the original MES implementer understands.",
                "problem": "Equipment failures hide in four-thousand-row reports. Your fab loses a percent of yield every month and nobody can explain why until the quarterly review.",
                "solution": "We map your MES schema, embed an AI layer that speaks your domain language, and ship a daily morning brief. It surfaces the four patterns costing you the most yield, ranked by impact, with citations back to the source data.",
                "why": "Yield is margin. A single percent of yield recovery on a 200mm fab is worth millions per quarter. Faster anomaly resolution means less scrap, fewer holds, and engineers spending their time fixing problems instead of hunting for them.",
                "examples": [
                    "Daily Pareto brief (top 20 holds ranked by yield impact, delivered at 7am)",
                    "Plain-English query layer over MES, LIMS, and SPC tables",
                    "Anomaly stratification by tool, chamber, recipe, and shift",
                    "Read-only connectors (we never write to your systems)",
                    "Audit log on every query (reviewable by your security team)",
                ],
            },
            {
                "glyph": "star",
                "practice_heading": "WHAT WE DELIVER",
                "title": "Your ERP holds the answer to every supply chain question.",
                "intro": "It just speaks SQL.",
                "problem": "Planners cannot ask \"why are we out of stock on SKU 47?\" without paging the data team. Forecasts get rebuilt by hand every Monday. Lead times slip and nobody explains why until the post-mortem.",
                "solution": "We wire an AI layer to your ERP inventory, shipments, and forecasts. Plain-language queries return live answers. \"Where is the shortfall coming from?\" gets answered in seconds, not days. Row-level security mirrors your existing access controls.",
                "why": "Visibility is leverage. The faster a planner can answer \"where is the shortfall coming from?\" the faster you can place a corrective order, route around a delay, or escalate to a supplier. Days of latency become minutes.",
                "examples": [
                    "Natural-language inventory and shipment queries",
                    "Forecast reconciliation (AI explains why the forecast moved week-over-week)",
                    "Slack alerts when key SKUs trip a threshold (with the reason already drafted)",
                    "Read-only connectors (no writes to your source systems)",
                    "Integration with your existing IAM (same access controls you already have)",
                ],
            },
            {
                "glyph": "flower",
                "practice_heading": "SYSTEMS WE KNOW",
                "title": "We work with your existing systems.",
                "intro": "",
                "problem": "Most teams already have the data. The gap is safe, explainable access aligned to how you govern access today.",
                "solution": "Most of our work integrates with MES (Apriso, Parsable, Wonderware), ERP (SAP, Oracle, NetSuite), quality/SPC (JMP, Minitab, custom databases), and warehouses (Snowflake, BigQuery, custom setups). Have a custom system or older legacy stack? We work with that too. We've debugged these systems for 18 years. We know where the data lives and how to read it safely.",
                "why": "You keep your stack. We add a read-only intelligence layer your team can query and trust.",
                "examples": [
                    "MES: Apriso, Parsable, Wonderware",
                    "ERP: SAP, Oracle, NetSuite",
                    "Quality/SPC: JMP, Minitab, custom databases",
                    "Data warehouse: Snowflake, BigQuery, custom setups",
                ],
            },
        ],
        "process_eyebrow": "Together",
        "process_headline": "How we work together",
        "process_subline": "",
        "process": [
            (
                "WEEK 1: DIAGNOSTIC CALL",
                "You describe your MES stack, your biggest operational pain, and what success looks like. We ask about data access, compliance requirements, and your timeline.",
            ),
            (
                "WEEK 2–3: SYSTEM AUDIT",
                "We map your MES schema, talk to your implementation team, and document every table we'll need. We deliver an audit report with our findings and recommendations.",
            ),
            (
                "WEEK 4–6: AI INTEGRATION",
                "We build read-only connectors, set up audit logging, and integrate with your security infrastructure. We test in a safe environment. No writes to your live systems.",
            ),
            (
                "WEEK 7+: GO LIVE",
                "We ship the daily brief, the query layer, the Slack alerts. Your team uses it Monday morning. We iterate weekly based on feedback until the artifact is the most-clicked link in your operations Slack.",
            ),
        ],
        "stats": [
            ("Read-only default", "Writes only with explicit approval"),
            ("Full audit trail", "Every query logged and reviewable"),
            ("You own the output", "Briefs, connectors, and code are yours"),
        ],
        "pricing": [
            (
                "Diagnostic audit: $20,000 (2 weeks)",
                "We map your systems, identify bottlenecks, and deliver a detailed report with recommendations. You decide if you want to proceed.",
            ),
            (
                "Full implementation: $75,000–$150,000 (4–6 weeks)",
                "Custom pricing based on system complexity, data volume, and integrations required. We quote after the diagnostic and you approve before we start building.",
            ),
            (
                "Ongoing retainer (optional): $5,000–$10,000/month",
                "Monthly iterations, new queries, new integrations as your business changes. Most clients don't need this—your team owns the system—but some prefer ongoing support.",
            ),
        ],
    },
    {
        "id": "personal",
        "label": "Individuals",
        "title_attr": esc("Small tools, flat fees, code on your machine—no retainer, no vendor lock-in."),
        "accent": "#7C3AED",
        "eyebrow": "For individuals & solo operators",
        "headline": "You have a system that works for everything.",
        "headline_em": "It's broken.",
        "lede": "Your files are scattered across five apps. Your notes live in three places. Your decisions get re-litigated because nobody can find the original thinking. "
        "You spend two hours a week on tasks that should take ten minutes.\n\n"
        "You don't need a bigger system. You need to automate the boring parts so you can focus on the work that matters.\n\n"
        "We build small, AI-powered tools that live on your machine or plug into your existing apps. No retainer. No vendor lock-in. You own the code and you can edit it yourself.",
        "cards": [
            {
                "glyph": "qf",
                "practice_heading": "WHAT WE BUILD",
                "title": "Ten thousand files on your desktop is not a filing system.",
                "intro": "It's a tax.",
                "problem": "You can't find anything. You re-create documents you already wrote. You search for 30 minutes and give up halfway through.",
                "solution": "We design a folder structure that fits how you actually work, auto-file every existing file, and build a personal search index. You ask a question in plain English and get back a file path. No more hunting.",
                "why": "A working filing system saves you hours a week and removes a constant low-grade frustration. More importantly, it protects work you've already done. Knowledge you can't find is knowledge you don't have.",
                "examples": [
                    "Custom folder structure (based on your actual projects, not templates)",
                    "Auto-tagging and auto-filing (for new files going forward)",
                    "Plain-English search (across docs, screenshots, and notes)",
                    "Integration with Finder/Explorer (no new app to learn)",
                ],
            },
            {
                "glyph": "star",
                "practice_heading": "WHAT WE BUILD",
                "title": "Two hours a week on copying, organizing, and sending the same email three times.",
                "intro": "",
                "problem": "The boring parts of your work are repetitive, predictable, and small enough that you keep doing them by hand. They never get fixed because they're not big enough to schedule a project around.",
                "solution": "We build small, focused scripts that run on a schedule. Inbox triage. Weekly report rollups. File rename batches. Calendar audits. Your personal assistant runs overnight. You wake up to a tidier desk.",
                "why": "These tasks are the unsexy ones, but they add up. Reclaiming two hours a week of focused time is the difference between shipping the project and not shipping it. Small leverage, applied weekly, is enormous.",
                "examples": [
                    "Inbox triage (auto-filters, draft replies in your voice)",
                    "Weekly report rollups (built from raw data, sent to your team)",
                    "Calendar audits (flags meetings without agendas or with the wrong people)",
                    "File organize batches (renames, archives old files, moves to the right folders)",
                ],
            },
            {
                "glyph": "flower",
                "practice_heading": "WHAT WE BUILD",
                "title": "You've solved this problem before.",
                "intro": "You forgot you did.",
                "problem": "Your past thinking is one of your most valuable assets. But your notes live in six apps and you can't find anything. Decisions get re-litigated. Problems get solved twice.",
                "solution": "We build a searchable knowledge graph indexed across all your sources. Ask \"what did I decide about X?\" and get the answer with a citation back to the original source. Your past self becomes your best collaborator.",
                "why": "Your past thinking compounds over time. A real personal knowledge base lets you build on it instead of reinventing it. It also reduces the anxiety of forgetting something important, because nothing is actually forgotten.",
                "examples": [
                    "Indexing across Notion, Apple Notes, Google Docs, voice memos, and emails",
                    "Plain-English Q&A (with citations back to the original source)",
                    "Weekly digest (of decisions and open threads you might have forgotten)",
                    "Integration with your existing workflow (no new tool to learn)",
                ],
            },
        ],
        "process_eyebrow": "Together",
        "process_headline": "How we work together",
        "process_subline": "",
        "process": [
            (
                "WEEK 1: FREE DISCOVERY CALL",
                "You tell us what's boring you. We listen, ask questions, and tell you honestly whether a small tool can fix it.",
            ),
            (
                "WEEK 2–3: QUOTE + TIMELINE",
                "A flat, one-time fee. No retainers. No surprises. You see the price before we start and the date before we build.",
            ),
            (
                "WEEK 4–6: BUILD + DEPLOY",
                "We build the tool on your machine or integrated with your apps. We walk you through how it works. You own the code. You can edit it. You can pass it on.",
            ),
        ],
        "stats": [
            ("Free discovery", "Straight talk before any fee"),
            ("Flat fee", "Price and delivery date upfront"),
            ("You own it", "Runs on your machine, your rules"),
        ],
        "pricing": [
            (
                "Free discovery call · custom quote for build",
                "We'll spend 30 minutes understanding what's actually wasting your time. Then we'll give you a flat fee and a clear delivery date. "
                "Most individual projects run $2,000–$8,000 depending on complexity.\n\n"
                "No retainers. You pay once. You own it forever.",
            )
        ],
    },
]


def glyph_svg(which, fill):
    """52px glyphs for long-card icon tile."""
    if which == "qf":
        return f"""<svg class="seg-svg" width="52" height="52" viewBox="-50 -50 100 100" aria-hidden="true">
          <path d="M0 -40 A 28 28 0 0 1 0 -8 A 28 28 0 0 1 0 -40 Z" fill="{fill}"/>
          <path d="M40 0 A 28 28 0 0 1 8 0 A 28 28 0 0 1 40 0 Z" fill="{fill}"/>
          <path d="M0 40 A 28 28 0 0 1 0 8 A 28 28 0 0 1 0 40 Z" fill="{fill}"/>
          <path d="M-40 0 A 28 28 0 0 1 -8 0 A 28 28 0 0 1 -40 0 Z" fill="{fill}"/>
          <circle r="5" fill="#fff"/>
        </svg>"""
    if which == "star":
        return f"""<svg class="seg-svg" width="52" height="52" viewBox="-50 -50 100 100" aria-hidden="true">
          <path d="M0 -44 L10 -10 L44 0 L10 10 L0 44 L-10 10 L-44 0 L-10 -10 Z" fill="{fill}"/>
          <circle r="4" fill="#fff"/>
        </svg>"""
    return f"""<svg class="seg-svg" width="52" height="52" viewBox="-50 -50 100 100" aria-hidden="true">
      <circle r="46" fill="{fill}"/>
      <circle r="38" fill="#fff"/>
      <g transform="scale(0.68)" fill="{fill}">
        <path d="M0 -40 A 28 28 0 0 1 0 -8 A 28 28 0 0 1 0 -40 Z"/>
        <path d="M40 0 A 28 28 0 0 1 8 0 A 28 28 0 0 1 40 0 Z"/>
        <path d="M0 40 A 28 28 0 0 1 0 8 A 28 28 0 0 1 0 40 Z"/>
        <path d="M-40 0 A 28 28 0 0 1 -8 0 A 28 28 0 0 1 -40 0 Z"/>
      </g>
      <circle r="3.5" fill="{fill}"/>
    </svg>"""


def long_card(seg_id, accent, _idx, card):
    g = card["glyph"]
    gfill = accent
    ph = esc(card.get("practice_heading", "WHAT WE DELIVER"))
    intro = card.get("intro", "").strip()
    ex_rows = "".join(
        f'''<div class="seg-ex-row{" seg-ex-first" if i == 0 else ""}">
           <span class="seg-ex-num">{str(i + 1).zfill(2)}</span><span>{esc(card["examples"][i])}</span>
         </div>'''
        for i in range(len(card.get("examples", [])))
    )
    intro_html = f'<p class="seg-long-intro">{esc(intro)}</p>' if intro else ""
    prob = card.get("problem", "").strip()
    sol = card.get("solution", "").strip()
    why = card.get("why", "").strip()
    blocks = ""
    if prob:
        blocks += f"""        <div class="seg-block">
          <div class="seg-block-label muted">The problem</div>
          <p class="seg-block-body">{esc(prob)}</p>
        </div>"""
    if sol:
        blocks += f"""        <div class="seg-block">
          <div class="seg-block-label accent-label">What we do</div>
          <p class="seg-block-body">{esc(sol)}</p>
        </div>"""
    if why:
        blocks += f"""        <div class="seg-block">
          <div class="seg-block-label accent-label">Why this matters</div>
          <p class="seg-block-body">{esc(why)}</p>
        </div>"""
    practice_block = ""
    if ex_rows:
        practice_block = f"""        <div class="seg-practice-card">
          <div class="seg-practice-heading">{ph}</div>
          {ex_rows}
        </div>"""
    return f"""
    <article class="seg-long-card" style="--seg-accent: {accent};">
      <div class="seg-long-left">
        <div class="seg-long-meta">
          <div class="seg-glyph-box">
            {glyph_svg(g, gfill)}
          </div>
        </div>
        <h3 class="seg-long-title">{esc(card["title"])}</h3>
        {intro_html}
      </div>
      <div class="seg-long-right">
{blocks}
{practice_block}
      </div>
    </article>"""


def pricing_html(seg):
    blocks = seg.get("pricing") or []
    if not blocks:
        return ""
    parts = []
    for title, body in blocks:
        paras = [esc(p).strip() for p in body.split("\n\n") if p.strip()]
        p_html = "".join(f"<p>{p}</p>" for p in paras)
        parts.append(
            f"""      <div class="seg-pricing-item">
        <h3 class="seg-pricing-title">{esc(title)}</h3>
        <div class="seg-pricing-body">{p_html}</div>
      </div>"""
        )
    return f"""
      <div class="seg-pricing-wrap">
        <span class="seg-eyebrow" style="--seg-accent: {seg['accent']}">Pricing</span>
        <h2 class="seg-pricing-headline">Transparent before you commit.</h2>
        {"".join(parts)}
      </div>"""


def panel(seg):
    sid = seg["id"]
    accent = seg["accent"]
    cards_html = "".join(long_card(sid, accent, i, c) for i, c in enumerate(seg["cards"]))
    proc_rows = []
    for i, (tt, bb) in enumerate(seg["process"]):
        proc_rows.append(
            f"""<div class="seg-step-row{' seg-step-last' if i == len(seg['process']) - 1 else ''}">
          <span class="seg-step-num">{str(i + 1).zfill(2)}</span>
          <div>
            <div class="seg-step-title">{esc(tt)}</div>
            <p class="seg-step-body">{esc(bb)}</p>
          </div>
        </div>"""
        )
    proc_html = "\n".join(proc_rows)

    pe = esc(seg.get("process_eyebrow", "How it works"))
    ph = esc(seg.get("process_headline", "Three steps."))
    ps = seg.get("process_subline", "")
    subline_html = f'<p class="seg-process-subline">{esc(ps)}</p>' if ps else ""

    stats_html = "".join(
        f"""<div class="seg-stat-card" style="--seg-accent: {accent}">
      <div class="seg-stat-big">{esc(n)}</div>
      <div class="seg-stat-sub">{esc(l)}</div>
    </div>"""
        for n, l in seg["stats"]
    )

    lede_paras = "".join(f"<p>{esc(p)}</p>" for p in seg["lede"].split("\n\n") if p.strip())

    return f"""
  <div class="seg-panel seg-panel-{sid}">
    <div class="seg-panel-inner container">
      <div class="seg-intro-grid">
        <div class="seg-intro-left">
          <span class="seg-eyebrow" style="--seg-accent: {accent}">{esc(seg['eyebrow'])}</span>
          <h2 class="seg-hero-headline">{esc(seg['headline'])}<br><span class="seg-hero-em">{esc(seg['headline_em'])}</span></h2>
        </div>
        <div class="seg-hero-lede-wrap">{lede_paras}</div>
      </div>

      <div class="seg-long-stack">
        {cards_html}
      </div>

      <div class="seg-process-grid">
        <div class="seg-process-left">
          <span class="seg-eyebrow" style="--seg-accent: {accent}">{pe}</span>
          <h2 class="seg-process-headline">{ph}</h2>
          {subline_html}
        </div>
        <div class="seg-process-rows">
          {proc_html}
        </div>
      </div>

      <div class="seg-stats-grid">
        {stats_html}
      </div>
{pricing_html(seg)}
    </div>
  </div>"""


def build_section():
    first = DATA[0]["id"]
    radios = "".join(
        f'  <input class="seg-rad" type="radio" name="who-segment" id="seg-{s["id"]}"{" checked" if s["id"] == first else ""}/>\n'
        for s in DATA
    )
    labels = "".join(
        f'        <label class="seg-tab seg-tab-{s["id"]}" for="seg-{s["id"]}" title="{s["title_attr"]}">{esc(s["label"])}</label>\n'
        for s in DATA
    )
    panels = "".join(panel(s) for s in DATA)
    body = (
        radios
        + '\n\n  <!-- WHO tabs -->\n  <div class="who-tab-strip" id="how-it-works">\n    <div class="container who-tab-inner">\n      <div class="who-tab-head">\n      <span class="who-banner-label">Who we serve</span>\n      <div class="seg-tab-group" role="tablist" aria-label="Audience">\n'
        + labels
        + '      </div>\n      </div>\n      <p class="who-tab-hint">Pick where you are. We meet you there.</p>\n    </div>\n  </div>\n\n  <div class="seg-panel-host">\n'
        + panels
        + "\n  </div>\n"
    )
    html_out = '<section class="who-we-serve" id="who-we-serve" aria-labelledby="who-banner">\n  <h2 class="sr-only" id="who-banner">Who we serve</h2>\n' + body + "</section>"
    return html_out


WHO_BLOCK = re.compile(
    r'<section class="who-we-serve"[\s\S]*?</section>\s*',
    re.MULTILINE,
)


def main():
    fragment = build_section()
    main_txt = INDEX.read_text(encoding="utf-8")
    if MARKER not in main_txt and 'id="who-we-serve"' not in main_txt:
        raise SystemExit("marker not found and no WHO section in index.html")
    if WHO_BLOCK.search(main_txt):
        main_txt = WHO_BLOCK.sub(fragment + "\n\n", main_txt, count=1)
        print("Replaced WHO WE SERVE section")
    else:
        if MARKER not in main_txt:
            raise SystemExit("marker not found in index.html")
        main_txt = main_txt.replace(MARKER, fragment + "\n\n" + MARKER, 1)
        print("Inserted WHO WE SERVE section")
    INDEX.write_text(main_txt, encoding="utf-8")


if __name__ == "__main__":
    main()

