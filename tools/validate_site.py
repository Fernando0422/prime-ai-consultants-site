"""Dependency-free validator for the Prime AI static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "index.html", "diagnostics.html", "methodology.html", "services.html",
    "ai-mes.html", "ai-erp.html", "ai-crm.html", "about.html", "contact.html",
    "privacy.html", "terms.html", "accessibility.html", "404.html",
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.hrefs, self.srcs = [], [], []
        self.h1 = self.title = self.description = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if attrs.get("href"):
            self.hrefs.append(attrs["href"])
        if attrs.get("src"):
            self.srcs.append(attrs["src"])
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title += 1
        if tag == "meta" and attrs.get("name") == "description" and attrs.get("content"):
            self.description += 1

errors = []
for name in PAGES:
    path = ROOT / name
    if not path.exists():
        errors.append(f"{name}: missing")
        continue
    source = path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(source)
    if parser.h1 != 1:
        errors.append(f"{name}: expected one h1, found {parser.h1}")
    if parser.title != 1 or parser.description != 1:
        errors.append(f"{name}: missing title or meta description")
    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        errors.append(f"{name}: duplicate ids {duplicates}")
    if re.search(r"\b(TBD|placeholder|starter|implementation notes)\b", source, re.I):
        errors.append(f"{name}: contains drafting language")
    if "\u2014" in source:
        errors.append(f"{name}: contains a customer-facing em dash")
    for target in parser.hrefs + parser.srcs:
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(("#", "mailto:", "tel:", "//")):
            continue
        local = parsed.path.lstrip("/") or "index.html"
        if "." not in Path(local).name:
            local += ".html"
        if not (ROOT / local).exists():
            errors.append(f"{name}: broken local reference {target}")

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
if sitemap.count("<url>") != 12:
    errors.append("sitemap.xml: expected 12 public routes")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(PAGES)} pages and 12 sitemap routes.")
