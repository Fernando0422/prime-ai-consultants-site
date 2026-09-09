# 2026-09-09 — Contact form: fix dead Gmail/Outlook handoff

Reported by Antonio: filling the contact form, clicking "Open email to send", then
picking Gmail in the browser/OS chooser did nothing. The page just sat there.

## Root cause

The contact form was mailto-only. On submit, `assets/site.js` built a
`mailto:hello@primeaiconsultants.com?...` URL and assigned it to
`window.location.href`. That hands the message to whatever mail handler the
visitor's operating system has registered for the `mailto:` protocol.

Visitors who use Gmail or Outlook on the web (no desktop mail client) have no
OS-level handler. When the browser/OS offers Gmail as an "open with" option,
Gmail cannot actually service a `mailto:` protocol URL, so the click dies
silently. This was a platform-level limitation of mailto, not fixable by
changing the mailto URL itself.

## Fix

After a valid submit, the page now shows three real options instead of firing a
blind mailto:

1. Send with Gmail: opens `https://mail.google.com/mail/?view=cm&fs=1&to=...&su=...&body=...` in a new tab.
2. Send with Outlook: opens the Outlook on the web compose deep link
   (`https://outlook.office.com/mail/deeplink/compose?to=...&subject=...&body=...`) in a new tab.
3. Open my email app: keeps the `mailto:` fallback for desktop mail clients.

Subject and body are pre-filled in every option; the existing 1800-character
length guard still applies so very long messages are truncated the same way for
all three providers.

Also fixed an adjacent layout issue found while testing: the form fields were
hidden after submit with the `hidden` attribute, but author CSS `display` rules
on those elements (`.contact-form-grid { display: grid }`) override `[hidden]`,
so the fields never actually collapsed. The JS now hides them via inline
`style.display = "none"`.

## Files changed

- `contact.html` — new success/chooser panel markup (ids `send-gmail`,
  `send-outlook`, `send-mailapp`).
- `assets/site.js` — submit handler now pre-fills the three compose links and
  reveals the chooser instead of navigating to `mailto:`.
- `assets/site.min.js` — synced copy of the same change.
- All 13 HTML pages — cache-buster bumped `site.min.js?v=mailto1` to
  `?v=mailto2` (the min assets are served with a 1-year immutable Cache-Control,
  so the version token must change for browsers to fetch the new file).
- `privacy.html` — wording updated to describe the Gmail/Outlook/email-app
  flow instead of "opens a draft in your email app".

## Verification

- JS syntax checked (`node --check`) on both assets.
- Playwright click-through (local preview and the live production site):
  - filling the form and submitting reveals the chooser panel;
  - all three links are pre-filled with the composed message;
  - clicking "Send with Gmail" opens a new tab to Gmail compose;
  - clicking "Send with Outlook" opens Outlook on the web compose;
  - mobile check at 390px: buttons stack full width, no horizontal scroll.
- Live site confirmed serving `site.min.js?v=mailto2` after the deploy.

No em dashes or banned words were introduced; the new copy follows the
existing contact-page tone.
