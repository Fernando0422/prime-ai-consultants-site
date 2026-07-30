#!/usr/bin/env python3
"""Replace top announce bar with bottom Ai4 toast; add page-site class to body."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ANNOUNCE_START = '  <div class="announce"'
ANNOUNCE_END = '  </div>\n\n  <nav class="site-nav"'

TOAST = '''  <aside class="ai4-toast" id="ai4-toast" role="region" aria-label="Ai4 conference" hidden>
    <div class="ai4-toast-inner">
      <span class="ai4-toast-tag">Ai4 2026</span>
      <p class="ai4-toast-text"><strong>Meet Prime AI</strong> Aug 4&ndash;6 &middot; The Venetian, Las Vegas.</p>
      <a href="contact.html#schedule" class="btn btn-primary btn-sm ai4-toast-cta">Book a meeting</a>
      <button type="button" class="ai4-toast-close" aria-label="Dismiss Ai4 notice">
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 3l10 10M13 3L3 13"/></svg>
      </button>
    </div>
  </aside>

  <nav class="site-nav"'''

TOAST_INDEX = TOAST.replace(
    'contact.html#schedule" class="btn btn-primary btn-sm ai4-toast-cta">Book a meeting</a>',
    'contact.html#schedule" class="btn btn-primary btn-sm ai4-toast-cta">Book a meeting</a>\n'
    '      <a href="#ai4" class="ai4-toast-details">Details</a>',
)

for path in ROOT.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    if ANNOUNCE_START not in text:
        continue
    start = text.index(ANNOUNCE_START)
    end = text.index('  <nav class="site-nav"', start)
    replacement = TOAST_INDEX if path.name == "index.html" else TOAST
    text = text[:start] + replacement + text[end + len('  <nav class="site-nav"'):]

    if 'class="page-site"' not in text and "<body" in text:
        text = text.replace(
            '<body class="page-home">',
            '<body class="page-home page-site">',
        )
        text = text.replace(
            '<body class="page-route">',
            '<body class="page-route page-site">',
        )
        text = text.replace(
            '<body class="page-methodology">',
            '<body class="page-methodology page-site">',
        )
        for marker in (
            'page-company',
            'page-services',
        ):
            old = f'<body class="page-route {marker}">'
            new = f'<body class="page-route page-site {marker}">'
            if old in text:
                text = text.replace(old, new)

    path.write_text(text, encoding="utf-8")
    print("patched", path.name)
