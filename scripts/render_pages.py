# -*- coding: utf-8 -*-
"""Emit interior HTML pages sharing nav/footer with index.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def extract_nav_footer():
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    i0 = idx.index("<!-- Primary navigation -->")
    i1 = idx.index("</nav>", i0)
    nav = idx[i0 : i1 + len("</nav>")]
    f0 = idx.index("<!-- ============== FOOTER ============== -->")
    f1 = idx.index('<script src="assets/site.js"', f0)
    footer = idx[f0:f1]
    return nav, footer


HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">
  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" media="all" data-prime-calendly-css="1">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <main id="main" tabindex="-1">
  <section class="page-hero hero" aria-labelledby="page-h1">
    <div class="hero-bg"></div>
    {nav}
    <div class="container page-hero-inner">
      <span class="pill">{pill}</span>
      <h1 class="page-title" id="page-h1">{h1}</h1>
      <p class="page-lede">{lede}</p>
    </div>
  </section>

  <div class="prose-page">
    <div class="container prose-stack">
{body}
    </div>
  </div>

  </main>

{footer}
  <script src="assets/site.js" defer></script>
</body>
</html>
"""


def write_page(fname: str, title: str, desc: str, pill: str, h1: str, lede: str, body: str) -> None:
    nav, footer = extract_nav_footer()
    out = HEAD.format(title=title, desc=desc, nav=nav, pill=pill, h1=h1, lede=lede, body=body.strip(), footer=footer)
    (ROOT / fname).write_text(out, encoding="utf-8")


def load_fragment(name: str) -> str:
    return (ROOT / "page_content" / name).read_text(encoding="utf-8")


def main() -> None:
    PAGE_CONTENT = ROOT / "page_content"
    if not PAGE_CONTENT.is_dir():
        raise SystemExit("Missing page_content/; create fragment files first.")

    write_page(
        "services.html",
        "Services | Prime AI Consultants",
        "Nine pillars of AI services: strategy, training, integration, reporting, automation, development, audits, managed services, and executive innovation.",
        "What we deliver",
        "Services built for ERP, CRM, and MES reality",
        "Structured engagements from readiness and roadmap work through integrations, automation, reporting, training, and long-term adoption support.",
        load_fragment("services.frag.html"),
    )
    write_page(
        "ai-mes.html",
        "AI for MES | Prime AI Consultants",
        "How modern AI complements manufacturing execution systems - natural-language access to MES data, reporting, RCA, tribal knowledge capture, and a path to conversational manufacturing analytics.",
        "Manufacturing",
        "How AI like Claude can enhance an existing MES environment",
        "MES stays the system of record. AI reduces friction extracting insight, shortening report cycles, and helping engineers spend less time in SQL - and more time improving the line.",
        load_fragment("mes.frag.html"),
    )
    write_page(
        "ai-erp.html",
        "AI for ERP | Prime AI Consultants",
        "Natural-language access to ERP data, accelerated reporting, reduced IT backlog, assisted support - and a roadmap toward predictive ERP and enterprise-wide intelligence.",
        "Enterprise systems",
        "How AI like Claude can enhance an existing ERP environment",
        "ERP customizations accumulated over decades should not stay locked behind ticket queues and specialist skillsets. AI changes how finance, ops, sales, and IT collaborate around the same ledger.",
        load_fragment("erp.frag.html"),
    )
    write_page(
        "ai-crm.html",
        "AI for CRM | Prime AI Consultants",
        "CRM plus AI - conversational access to pipelines, smarter forecasting, cleaner activity hygiene, reduced admin backlog, and a clearer path to proactive customer intelligence.",
        "Customers & pipelines",
        "How AI like Claude can enhance an existing CRM environment",
        "Organizations invest years tailoring CRM - yet reporting and segmentation still bottleneck on admins and developers. AI helps revenue teams self-serve without sacrificing governance.",
        load_fragment("crm.frag.html"),
    )
    write_page(
        "ai-individuals.html",
        "AI for Individuals | Prime AI Consultants",
        "Personal AI training, small-business enablement, assistants, content services, retirement and lifestyle workflows, and customized adoption roadmaps for non-enterprise clients.",
        "Everyone else",
        "AI adoption for professionals, freelancers, and families",
        "Not every meaningful AI outcome requires an ERP rollout. These offerings focus on tangible personal productivity outcomes and repeatable habits.",
        load_fragment("individuals.frag.html"),
    )
    write_page(
        "levels-of-ai.html",
        "Three levels of AI adoption | Prime AI Consultants",
        "Awareness → Augmentation → Transformation: a pragmatic ladder for enterprises and leadership teams aligning AI ambition with governance and delivery risk.",
        "Framework",
        "The three levels of AI adoption",
        "Whether you lead a plant, a BU, or only your own inbox, maturity is less about hype and more about repeatable capability - safely compounded over time.",
        load_fragment("levels.frag.html"),
    )
    write_page(
        "contact.html",
        "Contact | Prime AI Consultants",
        "Book a 30-minute discovery call or send a detailed note. Straightforward guidance on ERP, CRM, and MES-aligned AI engagements, without sales pressure.",
        "Connect",
        "Contact Prime AI Consultants",
        "Prefer email? Reach hello@prime-ai.com. We reply with next steps tailored to manufacturing, CRM, ERP, or personal workflows.",
        load_fragment("contact.frag.html"),
    )
    write_page(
        "company.html",
        "Company | Prime AI Consultants",
        "Mission, principals, engagement principles, locations, and how Prime AI Consultants pairs deep enterprise systems fluency with modern AI tooling.",
        "Trust",
        "Who we are, and how we work",
        "We pair decades of semiconductor MES realities with disciplined product instincts so AI recommendations stay deployable, not slide-deck fiction.",
        load_fragment("company.frag.html"),
    )
    print("Wrote:", [p.name for p in sorted((ROOT.glob("*.html"))) if p.name != "index.html"])


if __name__ == "__main__":
    main()
