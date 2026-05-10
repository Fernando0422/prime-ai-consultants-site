/* =================================================================
   PRIME AI CONSULTANTS — site.js
   Lightweight client-side: mobile nav, active link, announcement
   dismiss, sticky CTA, scroll reveal, Formspree contact submit.
   ================================================================= */
(function () {
  "use strict";

  // ---------- Helpers ----------
  function pageFile() {
    var p = window.location.pathname.replace(/\\/g, "/");
    var segs = p.split("/").filter(Boolean);
    var last = segs.length ? segs[segs.length - 1].toLowerCase() : "";
    if (!last || last === "") return "index.html";
    return last;
  }

  // ---------- Active nav link ----------
  function setActiveNav() {
    var current = pageFile();
    var aiPages = ["ai-mes.html", "ai-erp.html", "ai-crm.html", "services.html"];
    document.querySelectorAll(".nav-links a[href]").forEach(function (a) {
      var href = (a.getAttribute("href") || "").trim().toLowerCase();
      if (!href || href.startsWith("mailto:") || href.startsWith("tel:")) return;
      var hrefFile = href.split("/").pop().split("#")[0] || "index.html";
      if (hrefFile === current) {
        a.classList.add("active");
      } else if (a.dataset.parent === "services" && aiPages.indexOf(current) !== -1) {
        a.classList.add("active");
      }
    });
  }

  // ---------- Mobile nav ----------
  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var wrap = document.querySelector(".site-nav");
    if (!toggle || !wrap) return;

    function setOpen(open) {
      wrap.classList.toggle("is-nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.documentElement.style.overflow = open ? "hidden" : "";
    }

    toggle.addEventListener("click", function () {
      setOpen(!wrap.classList.contains("is-nav-open"));
    });

    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 920px)").matches) setOpen(false);
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && wrap.classList.contains("is-nav-open")) {
        setOpen(false);
        toggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (!window.matchMedia("(max-width: 920px)").matches) {
        setOpen(false);
      }
    });
  }

  // ---------- Announcement bar dismiss ----------
  function initAnnounce() {
    var el = document.querySelector(".announce");
    if (!el) return;
    var key = "prime_announce_dismissed_v1";
    try {
      if (localStorage.getItem(key) === "1") {
        el.setAttribute("hidden", "");
        return;
      }
    } catch (e) { /* storage blocked */ }

    var btn = el.querySelector(".announce-close");
    if (!btn) return;
    btn.addEventListener("click", function () {
      el.setAttribute("hidden", "");
      try { localStorage.setItem(key, "1"); } catch (e) { /* ignore */ }
    });
  }

  // ---------- Sticky CTA ----------
  function initStickyCta() {
    var el = document.querySelector(".sticky-cta");
    if (!el) return;
    if (pageFile() === "contact.html") {
      el.style.display = "none";
      return;
    }

    var threshold = 480;
    var ticking = false;

    function update() {
      ticking = false;
      var y = window.scrollY || window.pageYOffset || 0;
      var docH = document.documentElement.scrollHeight;
      var winH = window.innerHeight;
      var nearBottom = y + winH > docH - 240;
      if (y > threshold && !nearBottom) {
        el.classList.add("is-visible");
      } else {
        el.classList.remove("is-visible");
      }
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(update);
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  // ---------- Scroll reveal ----------
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    els.forEach(function (el) { obs.observe(el); });
  }

  // ---------- Contact form (Formspree) ----------
  function initContactForm() {
    var form = document.getElementById("contact-form");
    if (!form) return;

    var status = form.querySelector(".form-status");
    var submit = form.querySelector('button[type="submit"]');

    function setStatus(message, kind) {
      if (!status) return;
      status.textContent = message;
      status.classList.remove("is-success", "is-error");
      status.classList.add("is-visible");
      status.classList.add(kind === "error" ? "is-error" : "is-success");
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;

      var endpoint = form.getAttribute("action") || "";
      var fd = new FormData(form);

      // Block submission if Formspree endpoint is still the placeholder.
      if (endpoint.indexOf("YOUR_FORM_ID") !== -1 || !endpoint) {
        setStatus(
          "Form endpoint not yet configured. Please email hello@primeaiconsultants.com directly.",
          "error"
        );
        return;
      }

      if (submit) {
        submit.disabled = true;
        submit.dataset.label = submit.textContent;
        submit.textContent = "Sending…";
      }

      fetch(endpoint, {
        method: "POST",
        body: fd,
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            setStatus(
              "Thanks. Your message reached us. We will respond within one business day.",
              "success"
            );
          } else {
            return res.json().then(function (data) {
              var msg = data && data.errors && data.errors.length
                ? data.errors.map(function (e) { return e.message; }).join(", ")
                : "Submission failed. Please email hello@primeaiconsultants.com directly.";
              setStatus(msg, "error");
            });
          }
        })
        .catch(function () {
          setStatus(
            "Network error. Please email hello@primeaiconsultants.com directly.",
            "error"
          );
        })
        .finally(function () {
          if (submit) {
            submit.disabled = false;
            if (submit.dataset.label) submit.textContent = submit.dataset.label;
          }
        });
    });
  }

  // ---------- Phase detail accordions (methodology, exclusive panels) ----------
  function initPhaseDetailAccordions() {
    var root = document.querySelector('.phase-detail-list--accordion');
    if (!root) return;

    var articles = root.querySelectorAll('.phase-detail--accordion');
    function closeAllPanels() {
      articles.forEach(function (other) {
        var p = other.querySelector('.phase-detail-panel');
        var b = other.querySelector('.phase-detail-trigger');
        if (p) p.hidden = true;
        if (b) b.setAttribute('aria-expanded', 'false');
      });
    }

    function openPanel(article) {
      var b = article.querySelector('.phase-detail-trigger');
      var p = article.querySelector('.phase-detail-panel');
      closeAllPanels();
      if (p) p.hidden = false;
      if (b) b.setAttribute('aria-expanded', 'true');
    }

    articles.forEach(function (article, idx) {
      var btn = article.querySelector('.phase-detail-trigger');
      var panel = article.querySelector('.phase-detail-panel');
      if (!btn || !panel) return;

      if (idx === 0) {
        panel.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
      } else {
        panel.hidden = true;
        btn.setAttribute('aria-expanded', 'false');
      }

      btn.addEventListener('click', function () {
        var openClicked = panel.hasAttribute('hidden');
        closeAllPanels();
        if (openClicked) {
          panel.hidden = false;
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });

    var hash = window.location.hash;
    var match = hash && hash.match(/^#phase-(\d{2})$/);
    if (match) {
      var targetId = 'phase-' + match[1];
      var targetArticle = document.getElementById(targetId);
      if (
        targetArticle &&
        targetArticle.classList.contains('phase-detail--accordion') &&
        root.contains(targetArticle)
      ) {
        openPanel(targetArticle);
      }
    }
  }

  // ---------- Smooth scroll for in-page anchors ----------
  function initAnchorScroll() {
    document.addEventListener("click", function (e) {
      var a = e.target && e.target.closest && e.target.closest('a[href^="#"]');
      if (!a) return;
      var hash = a.getAttribute("href");
      if (!hash || hash === "#") return;
      var target = document.querySelector(hash);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({ top: top, behavior: "smooth" });
      history.pushState(null, "", hash);
    });
  }

  // ---------- Init ----------
  function initAll() {
    setActiveNav();
    initMobileNav();
    initAnnounce();
    initStickyCta();
    initReveal();
    initContactForm();
    initAnchorScroll();
    initPhaseDetailAccordions();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
})();
