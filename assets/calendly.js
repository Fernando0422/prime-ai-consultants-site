(function () {
  "use strict";

  /**
   * Paste your Calendly event URL below, or assign window.PRIME_CALENDLY_URL in a script
   * before this file loads (recommended for deployments that inject at build time).
   * Example: https://calendly.com/your-org/30-minute-discovery
   */
  var DEFAULT_SCHEDULE_URL = "";

  function effectiveUrl() {
    var preset = typeof window.PRIME_CALENDLY_URL === "string" ? window.PRIME_CALENDLY_URL.trim() : "";
    if (preset) return preset;
    return (DEFAULT_SCHEDULE_URL || "").trim();
  }

  function isConfigured() {
    var u = effectiveUrl();
    return /^https:\/\/([\w.-]+\.)?calendly\.com\/[^\s]+\/?.*$/i.test(u);
  }

  function loadWidgetCss() {
    if (document.querySelector('link[data-prime-calendly-css="1"]')) return;
    var l = document.createElement("link");
    l.rel = "stylesheet";
    l.href = "https://assets.calendly.com/assets/external/widget.css";
    l.media = "all";
    l.setAttribute("data-prime-calendly-css", "1");
    document.head.appendChild(l);
  }

  function loadWidgetScript(done) {
    if (typeof window.Calendly !== "undefined" && typeof window.Calendly.initPopupWidget === "function") {
      done();
      return;
    }
    var existing = document.querySelector('script[data-prime-calendly-js="1"]');
    if (existing) {
      function finish() {
        done();
      }
      if (existing.getAttribute("data-loaded") === "1") {
        finish();
        return;
      }
      existing.addEventListener("load", function onload() {
        existing.removeEventListener("load", onload);
        existing.setAttribute("data-loaded", "1");
        finish();
      });
      existing.addEventListener("error", function onerr() {
        existing.removeEventListener("error", onerr);
        finish();
      });
      return;
    }
    loadWidgetCss();
    var s = document.createElement("script");
    s.src = "https://assets.calendly.com/assets/external/widget.js";
    s.async = true;
    s.defer = true;
    s.setAttribute("data-prime-calendly-js", "1");
    s.onload = function () {
      s.setAttribute("data-loaded", "1");
      done();
    };
    s.onerror = function () {
      done();
    };
    document.body.appendChild(s);
  }

  function toggleConfigHints(showHelp) {
    document.querySelectorAll(".calendly-config-hint").forEach(function (el) {
      el.hidden = !showHelp;
    });
    document.querySelectorAll(".calendly-inline-shell").forEach(function (el) {
      el.classList.toggle("calendly-inline-shell--empty", showHelp);
    });
  }

  function mountInlineWidgets() {
    var u = effectiveUrl();
    if (!isConfigured()) {
      toggleConfigHints(true);
      return;
    }
    toggleConfigHints(false);

    loadWidgetScript(function () {
      if (!window.Calendly || typeof Calendly.initInlineWidget !== "function") {
        return;
      }

      document.querySelectorAll("[data-calendly-inline]").forEach(function (host) {
        if (host.dataset.calMounted === "1") return;

        var raw = (host.getAttribute("data-url") || "").trim();
        var eventUrl = raw && /^https:\/\/([\w.-]+\.)?calendly\.com\//i.test(raw) ? raw : u;
        host.textContent = "";
        host.innerHTML = "";

        try {
          Calendly.initInlineWidget({
            url: eventUrl,
            parentElement: host,
          });
          host.dataset.calMounted = "1";
        } catch (err) {
          /* Fallback: popup still works via nav CTAs when configured */
        }
      });
    });
  }

  function bindPopupTriggers() {
    document.body.addEventListener("click", function (ev) {
      var trigger = ev.target.closest("[data-calendly-popup]");
      if (!trigger) return;

      var fall = (trigger.getAttribute("href") || "contact.html#schedule").trim();

      if (!isConfigured()) {
        return;
      }

      ev.preventDefault();
      loadWidgetScript(function () {
        if (window.Calendly && typeof Calendly.initPopupWidget === "function") {
          Calendly.initPopupWidget({ url: effectiveUrl() });
        } else {
          window.location.href = fall || "contact.html#schedule";
        }
      });
    });
  }

  function init() {
    mountInlineWidgets();
    bindPopupTriggers();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
