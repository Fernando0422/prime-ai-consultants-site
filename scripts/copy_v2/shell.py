# Shared HTML shell for legally conservative copy v2.0
# LinkedIn URL unresolved — links fall back to contact until set.

BUSINESS_EMAIL = "hello@primeaiconsultants.com"
PRIVACY_EMAIL = "hello@primeaiconsultants.com"
EFFECTIVE_DATE = "July 16, 2026"
# Leave empty until Fernando confirms the exact profile URL.
FERNANDO_LINKEDIN_URL = ""
FORM_PROCESSOR = "Formspree"
HOSTING_PROVIDER = "Vercel"
ANALYTICS_PROVIDER = "none"
CSS_VERSION = "flow12"

LINKEDIN_HREF = FERNANDO_LINKEDIN_URL or "contact.html"


def head(title, description, body_class, canonical_path, extra_fonts=""):
    fonts = (
        "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400"
        "&family=IBM+Plex+Mono:wght@400;500"
        + extra_fonts
        + "&display=swap"
    )
    canon = f"https://www.primeaiconsultants.com{canonical_path}"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script>document.documentElement.classList.add("js");</script>
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#F3F2EE" />
  <link rel="canonical" href="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{fonts}" rel="stylesheet" />
  <link rel="stylesheet" href="assets/styles.css" />
  <link rel="stylesheet" href="assets/enhancements.css?v={CSS_VERSION}" />
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />
  <link rel="apple-touch-icon" href="assets/logo/app-icon.svg" />
</head>
<body class="{body_class}">
  <a class="skip-link" href="#main">Skip to main content</a>
"""


def nav(active=""):
    def cls(name):
        return ' class="active"' if active == name else ""

    return f"""  <nav class="site-nav site-nav--light" aria-label="Primary navigation">
    <div class="nav-inner">
      <a class="brand" href="index.html" aria-label="Prime AI Consultants home">
        <img class="brand-logo" src="assets/prime-ai-logo-nav-on-light.svg" alt="" width="320" height="76" decoding="async" />
      </a>
      <ul class="nav-links" id="nav-links" role="list">
        <li class="nav-home-item"><a href="index.html"{cls("home")}>Home</a></li>
        <li><a href="diagnostics.html"{cls("diagnostics")}>Prime Diagnostics</a></li>
        <li><a href="methodology.html"{cls("methodology")}>Methodology</a></li>
        <li><a href="company.html"{cls("company")}>Company</a></li>
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


FOOTER = f"""  <footer class="footer footer--prime">
    <div class="container footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a class="footer-brand-logo-link" href="index.html"><img class="footer-brand-logo" src="assets/prime-ai-logo-nav-on-light.svg" alt="Prime AI Consultants" width="180" height="72" decoding="async" /></a>
          <p class="footer-tagline">Prime AI Consultants helps organizations document the systems, business rules, and operational knowledge behind AI and analytics initiatives before implementation&nbsp;begins.</p>
          <p class="footer-email"><a href="mailto:{BUSINESS_EMAIL}">{BUSINESS_EMAIL}</a></p>
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
              <li><a href="{LINKEDIN_HREF}" data-fernando-linkedin>LinkedIn</a></li>
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

  <script src="assets/site.js" defer></script>
</body>
</html>
"""


def page(title, description, body_class, canonical_path, active, main_html, extra_fonts=""):
    # Interior pages share the light shell; homepage keeps page-flow.
    if "page-home" not in body_class and "page-interior" not in body_class:
        body_class = f"{body_class} page-interior".strip()
    if "page-site" not in body_class:
        body_class = f"{body_class} page-site".strip()
    return (
        head(title, description, body_class, canonical_path, extra_fonts)
        + nav(active)
        + '  <main id="main" tabindex="-1">\n'
        + main_html
        + "\n  </main>\n\n"
        + FOOTER
    )
