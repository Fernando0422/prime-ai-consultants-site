#!/usr/bin/env python3
"""Unify nav/footer/head chrome across all HTML pages to match the homepage shell."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS_VERSION = "wrap1"

FOOTER = """  <footer class="footer footer--prime">
    <div class="container footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a class="footer-brand-logo-link" href="index.html"><img class="footer-brand-logo" src="assets/prime-ai-logo-nav-on-light.svg" alt="Prime AI Consultants" width="180" height="72" decoding="async" /></a>
          <p class="footer-tagline">Prime AI Consultants helps organizations document the systems, business rules, and operational knowledge behind AI and analytics initiatives before implementation&nbsp;begins.</p>
          <p class="footer-email"><a href="mailto:hello@primeaiconsultants.com">hello@primeaiconsultants.com</a></p>
        </div>
        <div class="footer-nav">
          <div class="footer-col">
            <h2 class="footer-col-title">Approach</h2>
            <ul>
              <li><a href="diagnostics.html">Prime Diagnostics</a></li>
              <li><a href="methodology.html">Methodology</a></li>
              <li><a href="services.html">Services</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h2 class="footer-col-title">Applications</h2>
            <ul>
              <li><a href="ai-mes.html">AI for MES</a></li>
              <li><a href="ai-erp.html">AI for ERP</a></li>
              <li><a href="ai-crm.html">AI for CRM</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h2 class="footer-col-title">Company</h2>
            <ul>
              <li><a href="company.html">Company</a></li>
              <li><a href="contact.html">Contact</a></li>
              <li><a href="contact.html" data-fernando-linkedin>LinkedIn</a></li>
            </ul>
          </div>
        </div>
      </div>

      <p class="footer-disclaimer">Information on this website is general and does not constitute legal, regulatory, cybersecurity, financial, compliance, or other professional advice. Engagement scope, deliverables, responsibilities, ownership, and limitations are defined in a written&nbsp;agreement.</p>

      <div class="footer-base">
        <span>&copy; 2026 Prime AI Consultants LLC. All rights reserved.</span>
        <span class="footer-legal">
          <a href="privacy.html">Privacy</a>
          <a href="terms.html">Terms</a>
          <a href="accessibility.html">Accessibility</a>
          <a href="contact.html">Contact</a>
        </span>
      </div>
    </div>
  </footer>
"""

ACTIVE_BY_FILE = {
    "index.html": "home",
    "diagnostics.html": "diagnostics",
    "methodology.html": "methodology",
    "company.html": "company",
    "contact.html": "contact",
    "services.html": "services",
    "ai-mes.html": "services",
    "ai-erp.html": "services",
    "ai-crm.html": "services",
    "privacy.html": "",
    "terms.html": "",
    "accessibility.html": "",
    "404.html": "",
}


def nav_html(active: str) -> str:
    def cls(name: str) -> str:
        return ' class="active"' if active == name else ""

    services_active = active == "services"
    parent_cls = ' class="nav-parent-link active"' if services_active else ' class="nav-parent-link"'
    overview_cls = ' class="active"' if services_active else ""
    # Child page actives are applied by setActiveNav in site.js; keep overview
    # highlighted when on services.html only (active == "services" covers AI pages
    # for the parent, but overview should only be active on services.html itself).
    # Rebuild does not know which AI page; site.js corrects child actives.

    return f"""  <nav class="site-nav site-nav--light" aria-label="Primary navigation">
    <div class="nav-inner">
      <a class="brand" href="index.html" aria-label="Prime AI Consultants home">
        <img class="brand-logo" src="assets/prime-ai-logo-nav-on-light.svg" alt="" width="320" height="76" decoding="async" />
      </a>
      <ul class="nav-links" id="nav-links" role="list">
        <li class="nav-home-item"><a href="index.html"{cls("home")}>Home</a></li>
        <li><a href="diagnostics.html"{cls("diagnostics")} aria-label="Prime Diagnostics">Diagnostics</a></li>
        <li><a href="methodology.html"{cls("methodology")}>Methodology</a></li>
        <li class="nav-item-has-sub">
          <a href="services.html"{parent_cls} data-parent="services" aria-haspopup="true" aria-expanded="false" aria-controls="nav-sub-services">Services</a>
          <ul class="nav-sub" id="nav-sub-services" role="list">
            <li><a href="services.html"{overview_cls}>Services overview</a></li>
            <li><a href="ai-mes.html">AI for MES</a></li>
            <li><a href="ai-erp.html">AI for ERP</a></li>
            <li><a href="ai-crm.html">AI for CRM</a></li>
          </ul>
        </li>
        <li><a href="company.html"{cls("company")}>About Us</a></li>
        <li><a href="contact.html"{cls("contact")}>Contact</a></li>
        <li class="nav-links-cta-item"><a href="contact.html" class="btn btn-primary btn-sm nav-links-cta-btn">Discuss your environment</a></li>
      </ul>
      <div class="nav-cta">
        <a href="contact.html" class="btn btn-primary btn-sm">Discuss your environment</a>
      </div>
      <button type="button" class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
        <span class="bars" aria-hidden="true"></span>
      </button>
    </div>
  </nav>
"""


def ensure_js_bootstrap(head: str) -> str:
    if 'classList.add("js")' in head:
        return head
    return re.sub(
        r'(<meta name="viewport"[^>]*>\s*)',
        r'\1  <script>document.documentElement.classList.add("js");</script>\n',
        head,
        count=1,
        flags=re.I,
    )


def patch_head(head: str) -> str:
    head = ensure_js_bootstrap(head)
    head = re.sub(
        r'<meta name="theme-color" content="[^"]*"\s*/?>',
        '<meta name="theme-color" content="#F3F2EE" />',
        head,
        count=1,
        flags=re.I,
    )
    head = re.sub(
        r'href="assets/enhancements\.css(?:\?v=[^"]*)?"',
        f'href="assets/enhancements.css?v={CSS_VERSION}"',
        head,
        count=1,
    )
    return head


def extract_main(html: str) -> str:
    m = re.search(r"(<main\b[^>]*>[\s\S]*?</main>)", html, re.I)
    if not m:
        raise ValueError("No <main> found")
    return m.group(1)


def extract_head(html: str) -> str:
    m = re.search(r"(<head\b[^>]*>[\s\S]*?</head>)", html, re.I)
    if not m:
        raise ValueError("No <head> found")
    return m.group(1)


def extract_body_class(html: str) -> str:
    m = re.search(r"<body\b([^>]*)>", html, re.I)
    if not m:
        return 'class="page-site"'
    attrs = m.group(1)
    cm = re.search(r'class="([^"]*)"', attrs)
    if not cm:
        return 'class="page-site"'
    classes = cm.group(1).split()
    if "page-site" not in classes:
        classes.append("page-site")
    # Interior pages get light shell class for shared hero/nav theming
    if "page-home" not in classes and "page-interior" not in classes:
        classes.append("page-interior")
    return f'class="{" ".join(classes)}"'


def rebuild(path: Path) -> None:
    html = path.read_text()
    name = path.name
    active = ACTIVE_BY_FILE.get(name, "")
    head = patch_head(extract_head(html))
    main = extract_main(html)
    body_class = extract_body_class(html)

    # Content polish for specific pages
    if name == "diagnostics.html":
        main = main.replace(
            "Request a Diagnostics conversation",
            "Discuss Prime Diagnostics",
        )
    if name == "company.html":
        main = main.replace(
            "Co-Founder — Operational Systems",
            "Co-Founder — Enterprise Applications and Operational Systems",
        )
        main = main.replace(
            "Co-Founder — Strategy and Service Design",
            "Co-Founder — Strategy, Service Design, and Client Experience",
        )
        main = main.replace(
            'alt="Antonio Rojas, Co-Founder — Operational Systems"',
            'alt="Antonio Rojas, Co-Founder — Enterprise Applications and Operational Systems"',
        )
        main = main.replace(
            'alt="Fernando Rojas, Co-Founder — Strategy and Service Design"',
            'alt="Fernando Rojas, Co-Founder — Strategy, Service Design, and Client Experience"',
        )

    out = (
        "<!doctype html>\n"
        '<html lang="en">\n'
        f"{head}\n"
        f"<body {body_class}>\n"
        '  <a class="skip-link" href="#main">Skip to main content</a>\n'
        f"{nav_html(active)}"
        f"{main}\n\n"
        f"{FOOTER}\n"
        '  <script src="assets/site.js" defer></script>\n'
        "</body>\n"
        "</html>\n"
    )
    path.write_text(out)
    print(f"updated {name}")


def main() -> None:
    for path in sorted(ROOT.glob("*.html")):
        rebuild(path)


if __name__ == "__main__":
    main()
