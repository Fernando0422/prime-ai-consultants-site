/* =================================================================
   PRIME AI CONSULTANTS — site.js
   Lightweight client-side: mobile nav, active link, announcement
   dismiss, sticky CTA, scroll reveal, Formspree contact submit.
   ================================================================= */
(function () {
  "use strict";

  // Set your Formspree form ID from https://formspree.io (e.g. "xrgvabcd").
  // Leave empty to show a clear error and direct visitors to email instead.
  var FORMSPREE_FORM_ID = "xgoqorke";

  // ---------- Helpers ----------
  function pageFile() {
    var p = window.location.pathname.replace(/\\/g, "/");
    var segs = p.split("/").filter(Boolean);
    var last = segs.length ? segs[segs.length - 1].toLowerCase() : "";
    if (!last || last === "") return "index.html";
    return last;
  }

  // ---------- Active nav link ----------
  function parseNavHref(href) {
    var raw = (href || "").trim().toLowerCase();
    if (!raw || raw.startsWith("mailto:") || raw.startsWith("tel:")) return null;
    var parts = raw.split("#");
    var file = parts[0].split("/").pop() || "index.html";
    var hash = parts.length > 1 ? "#" + parts[1] : "";
    return { file: file, hash: hash };
  }

  function setActiveNav() {
    var current = pageFile();
    var currentHash = (window.location.hash || "").toLowerCase();
    var aiPages = ["ai-mes.html", "ai-erp.html", "ai-crm.html", "services.html"];
    document.querySelectorAll(".nav-links a[href], .nav-parent-link[href]").forEach(function (a) {
      var parsed = parseNavHref(a.getAttribute("href"));
      if (!parsed) return;
      if (parsed.file === current) {
        if (parsed.hash === currentHash) {
          a.classList.add("active");
        } else if (!parsed.hash && !currentHash) {
          a.classList.add("active");
        }
      } else if (a.dataset.parent === "services" && aiPages.indexOf(current) !== -1) {
        a.classList.add("active");
      }
    });
  }

  // ---------- Mobile nav ----------
  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var wrap = document.querySelector(".site-nav");
    var navLinks = document.querySelector(".nav-links");
    if (!toggle || !wrap) return;

    if (navLinks && !navLinks.id) {
      navLinks.id = "nav-links";
    }

    var focusTrapHandler = null;

    function mobileMenuFocusables() {
      var list = [toggle];
      if (navLinks) {
        navLinks.querySelectorAll('a[href], button:not([disabled])').forEach(function (el) {
          list.push(el);
        });
      }
      return list.filter(function (el) {
        return el && !el.disabled && el.offsetParent !== null;
      });
    }

    function trapMenuFocus(e) {
      if (e.key !== "Tab" || !wrap.classList.contains("is-nav-open")) return;
      var items = mobileMenuFocusables();
      if (items.length < 2) return;
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }

    function setOpen(open) {
      wrap.classList.toggle("is-nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.documentElement.style.overflow = open ? "hidden" : "";

      if (open) {
        if (!focusTrapHandler) {
          focusTrapHandler = trapMenuFocus;
          document.addEventListener("keydown", focusTrapHandler);
        }
        var items = mobileMenuFocusables();
        var firstLink = navLinks ? navLinks.querySelector("a[href]") : null;
        window.requestAnimationFrame(function () {
          if (firstLink) firstLink.focus();
          else if (items[0]) items[0].focus();
        });
      } else if (focusTrapHandler) {
        document.removeEventListener("keydown", focusTrapHandler);
        focusTrapHandler = null;
      }
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

  // ---------- Ai4 bottom toast (conference window only) ----------
  function initAi4Toast() {
    var el = document.querySelector(".ai4-toast");
    if (!el) return;

    var end = new Date("2026-08-07T00:00:00");
    if (Date.now() >= end.getTime()) {
      el.setAttribute("hidden", "");
      return;
    }

    var storageKey = "prime_ai4_toast_dismissed_v2";
    try {
      if (localStorage.getItem(storageKey) === "1") {
        el.setAttribute("hidden", "");
        return;
      }
    } catch (e) { /* storage blocked */ }

    var hero =
      document.querySelector(".hero") ||
      document.querySelector(".page-hero");
    var dismissedScroll = false;

    function hideToast(persist) {
      el.setAttribute("hidden", "");
      el.classList.remove("is-visible");
      document.body.classList.remove("has-ai4-toast");
      if (persist) {
        try { localStorage.setItem(storageKey, "1"); } catch (err) { /* ignore */ }
      }
    }

    function showToast() {
      el.removeAttribute("hidden");
      el.classList.add("is-visible");
      document.body.classList.add("has-ai4-toast");
    }

    showToast();

    var closeBtn = el.querySelector(".ai4-toast-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        hideToast(true);
      });
    }

    function onScroll() {
      if (dismissedScroll || !hero) return;
      var heroBottom = hero.getBoundingClientRect().bottom;
      if (heroBottom < 0) {
        dismissedScroll = true;
        hideToast(false);
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
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
    var visible = false;

    function update() {
      ticking = false;
      var y = window.scrollY || window.pageYOffset || 0;
      var docH = document.documentElement.scrollHeight;
      var winH = window.innerHeight;
      var nearBottom = y + winH > docH - 240;
      var shouldShow = y > threshold && !nearBottom;
      if (shouldShow === visible) return;
      visible = shouldShow;
      el.classList.toggle("is-visible", shouldShow);
      document.body.classList.toggle("has-sticky-cta", shouldShow);
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(update);
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", update, { passive: true });
    update();
  }

  // ---------- Scroll reveal ----------
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;

    if (
      !("IntersectionObserver" in window) ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ) {
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
    }, { rootMargin: "0px 0px -4% 0px", threshold: 0.12 });
    els.forEach(function (el) { obs.observe(el); });
  }

  // ---------- Contact form (Formspree) ----------
  function initContactForm() {
    var form = document.getElementById("contact-form");
    if (!form) return;

    if (FORMSPREE_FORM_ID) {
      form.setAttribute("action", "https://formspree.io/f/" + FORMSPREE_FORM_ID);
    }

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
      if (!endpoint && FORMSPREE_FORM_ID) {
        endpoint = "https://formspree.io/f/" + FORMSPREE_FORM_ID;
        form.setAttribute("action", endpoint);
      }
      var fd = new FormData(form);

      // Block submission if Formspree endpoint is still the placeholder.
      if (!FORMSPREE_FORM_ID || endpoint.indexOf("YOUR_FORM_ID") !== -1 || !endpoint) {
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

  // ---------- Stat counter animation ----------
  function initStatCounters() {
    var counters = document.querySelectorAll("[data-count]");
    if (!counters.length) return;

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      counters.forEach(function (el) {
        el.textContent = el.getAttribute("data-count") || el.textContent;
      });
      return;
    }

    function animateCount(el, target, duration) {
      var start = 0;
      var startTime = null;
      function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(start + (target - start) * eased);
        if (progress < 1) window.requestAnimationFrame(step);
        else el.textContent = target;
      }
      window.requestAnimationFrame(step);
    }

    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseInt(el.getAttribute("data-count"), 10);
        if (isNaN(target)) return;
        animateCount(el, target, 1200);
        obs.unobserve(el);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { obs.observe(el); });
  }

  // ---------- Proof card expand/collapse ----------
  function initProofToggle() {
    document.querySelectorAll(".proof-card-toggle").forEach(function (btn) {
      var panelId = btn.getAttribute("aria-controls");
      var panel = panelId ? document.getElementById(panelId) : null;
      if (!panel) return;
      btn.addEventListener("click", function () {
        var open = panel.hasAttribute("hidden");
        panel.hidden = !open;
        btn.setAttribute("aria-expanded", open ? "true" : "false");
        var textNode = Array.prototype.find.call(btn.childNodes, function (n) {
          return n.nodeType === 3;
        });
        if (textNode) {
          textNode.textContent = open ? "Hide full story " : "Read full story ";
        }
      });
    });
  }

  // ---------- Path selector → engage card highlight ----------
  function initPathSelector() {
    var cards = document.querySelectorAll(".path-card[data-engage-target]");
    var engageCards = document.querySelectorAll(".engage-card[id]");
    if (!cards.length) return;

    function highlight(id) {
      engageCards.forEach(function (c) {
        c.classList.toggle("is-highlight", c.id === id);
      });
      cards.forEach(function (p) {
        p.classList.toggle("is-active", p.getAttribute("data-engage-target") === id);
      });
    }

    cards.forEach(function (card) {
      card.addEventListener("mouseenter", function () {
        highlight(card.getAttribute("data-engage-target"));
      });
      card.addEventListener("focus", function () {
        highlight(card.getAttribute("data-engage-target"));
      });
    });

    if (window.location.hash) {
      var id = window.location.hash.replace("#", "");
      if (document.getElementById(id)) highlight(id);
    } else {
      highlight("diagnostics");
    }
  }

  // ---------- Smooth scroll for in-page anchors ----------
  function initAnchorScroll() {
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    document.addEventListener("click", function (e) {
      var a = e.target && e.target.closest && e.target.closest('a[href^="#"]');
      if (!a) return;
      var hash = a.getAttribute("href");
      if (!hash || hash === "#") return;
      var target = document.querySelector(hash);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({ top: top, behavior: reduceMotion ? "auto" : "smooth" });
      history.pushState(null, "", hash);
    });
  }

  // ---------- Hero / pitch background videos (optional assets/hero/*) ----------
  function initOptionalVideo(video, onReady) {
    if (!video) return;

    function markReady() {
      video.classList.add("is-ready");
      if (onReady) onReady();
    }

    video.addEventListener("loadeddata", markReady);
    video.addEventListener("canplay", markReady);

    if (video.readyState >= 2) {
      markReady();
    } else {
      video.addEventListener("error", function () {
        if (video.classList.contains("hero-bg-video")) {
          video.remove();
        }
      });
    }
  }

  function initHeroVideo() {
    initOptionalVideo(document.querySelector(".hero-bg-video"));
    initOptionalVideo(document.querySelector(".pitch-video-el"));
  }

  // ---------- Industry explorer (Where this applies) ----------
  function initIndustryExplorer() {
    var tablist = document.querySelector(".industries-browser-nav[role='tablist']");
    if (!tablist) return;

    var tabs = tablist.querySelectorAll("[role='tab']");

    function activate(tab) {
      var panelId = tab.getAttribute("aria-controls");
      tabs.forEach(function (t) {
        var selected = t === tab;
        t.setAttribute("aria-selected", selected ? "true" : "false");
        t.tabIndex = selected ? 0 : -1;
      });
      document.querySelectorAll(".industry-panel").forEach(function (panel) {
        var isActive = panel.id === panelId;
        panel.classList.toggle("is-active", isActive);
        panel.hidden = !isActive;
      });
    }

    tabs.forEach(function (tab, index) {
      tab.tabIndex = tab.getAttribute("aria-selected") === "true" ? 0 : -1;
      tab.addEventListener("click", function () {
        activate(tab);
        if (window.matchMedia("(max-width: 820px)").matches) {
          tab.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
        }
      });
      tab.addEventListener("keydown", function (e) {
        var next = -1;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") {
          next = (index + 1) % tabs.length;
        } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
          next = (index - 1 + tabs.length) % tabs.length;
        } else if (e.key === "Home") {
          next = 0;
        } else if (e.key === "End") {
          next = tabs.length - 1;
        }
        if (next >= 0) {
          e.preventDefault();
          activate(tabs[next]);
          tabs[next].focus();
        }
      });
    });
  }

  // ---------- Init ----------
  function initAll() {
    setActiveNav();
    initMobileNav();
    initAi4Toast();
    initStickyCta();
    initHeroVideo();
    initIndustryExplorer();
    initReveal();
    initContactForm();
    initAnchorScroll();
    initPhaseDetailAccordions();
    initStatCounters();
    initProofToggle();
    initPathSelector();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
})();
