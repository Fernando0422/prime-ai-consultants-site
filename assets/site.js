(function () {
  "use strict";

  function pathnameFile() {
    var pathname = window.location.pathname.replace(/\\/g, "/");
    var segments = pathname.split("/").filter(Boolean);
    var last = segments.length ? segments[segments.length - 1] : "";
    if (!last || last.toLowerCase() === "index.html") return "index.html";
    return last;
  }

  function parseHrefNav(href) {
    href = href.trim();
    var q = href.indexOf("?");
    if (q >= 0) href = href.slice(0, q);
    var hashIdx = href.indexOf("#");
    var hashPart = hashIdx >= 0 ? href.slice(hashIdx).toLowerCase() : "";
    var pathPart = hashIdx >= 0 ? href.slice(0, hashIdx) : href;
    var segments = pathPart.split("/").filter(Boolean);
    var file =
      segments.length === 0
        ? ""
        : segments[segments.length - 1].toLowerCase() || "index.html";
    if (!file.endsWith(".html") && segments.length === 0) file = "";
    if (
      segments.length &&
      segments[segments.length - 1] === "" &&
      !file.endsWith(".html")
    )
      file = "index.html";
    return { file: file, hash: hashPart };
  }

  function closeAllNavDropdowns() {
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (dd) {
      dd.classList.remove("is-open");
      var t = dd.querySelector(".nav-dropdown-toggle");
      if (t) t.setAttribute("aria-expanded", "false");
    });
  }

  function setNavActiveByPathname() {
    var current = pathnameFile().toLowerCase();
    var pageHash = (window.location.hash || "").toLowerCase();
    var onHomePage = current === "index.html" || current === "";

    document.querySelectorAll(".nav-sheet [data-nav-dropdown]").forEach(function (dd) {
      dd.classList.remove("nav-dropdown-parent-active");
    });

    document.querySelectorAll(".nav-sheet a").forEach(function (a) {
      a.classList.remove("active");
    });

    document.querySelectorAll(".nav-sheet a").forEach(function (a) {
      var href = a.getAttribute("href") || "";
      if (
        !href.trim() ||
        href.startsWith("mailto:") ||
        href.startsWith("javascript:")
      ) {
        return;
      }

      var parsed = parseHrefNav(href);
      var hrefFile = parsed.file.toLowerCase();
      if (!hrefFile && !parsed.hash) return;

      var active = false;

      if (hrefFile === "index.html" && parsed.hash === "") {
        active = onHomePage;
      } else if (hrefFile) {
        var fileMatches =
          hrefFile === current || (hrefFile === "index.html" && onHomePage);
        if (parsed.hash) active = fileMatches && pageHash === parsed.hash;
        else active = hrefFile === current;
      } else if (parsed.hash && onHomePage) {
        active = pageHash === parsed.hash;
      }

      if (active) {
        a.classList.add("active");
      }
    });

    document.querySelectorAll("[data-nav-dropdown]").forEach(function (dd) {
      if (
        dd.querySelector(".nav-dropdown-panel a.active") ||
        dd.querySelector("a.nav-dropdown-primary.active")
      ) {
        dd.classList.add("nav-dropdown-parent-active");
      }
    });
  }

  function initDiscoveryForm() {
    var discoveryForm = document.getElementById("discovery-form");
    if (!discoveryForm) return;
    discoveryForm.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!discoveryForm.reportValidity()) return;

      var fd = new FormData(discoveryForm);
      var msg = fd.get("message");
      msg = typeof msg === "string" ? msg : "";
      if (msg.length > 1200) {
        msg = msg.slice(0, 1170) + "\n…(message truncated)";
      }

      var bodyLines = [
        "Discovery call: website form",
        "",
        "First: " + (fd.get("firstName") || ""),
        "Last: " + (fd.get("lastName") || ""),
        "Email: " + (fd.get("email") || ""),
        "Phone: " + (fd.get("phone") || ""),
        "Company: " + (fd.get("company") || ""),
        "",
        "Message:",
        msg,
      ];
      var subject = encodeURIComponent(
        "Discovery call: " + String(fd.get("company") || "website inquiry")
      );
      var mailtoUrl =
        "mailto:hello@prime-ai.com?subject=" +
        subject +
        "&body=" +
        encodeURIComponent(bodyLines.join("\n"));

      if (mailtoUrl.length > 1850) {
        window.location.href =
          "mailto:hello@prime-ai.com?subject=" +
          subject +
          "&body=" +
          encodeURIComponent(
            "(Message was long - please reply with details.)\n\nCompany: " +
              String(fd.get("company") || "") +
              "\nEmail: " +
              String(fd.get("email") || "")
          );
        return;
      }
      window.location.href = mailtoUrl;
    });
  }

  function initContactFormAlias() {
    var form = document.getElementById("contact-main-form");
    if (!form) return;
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      var fd = new FormData(form);
      var subject = encodeURIComponent(
        String(fd.get("subject") || "Website contact | Prime AI Consultants")
      );
      var msg = fd.get("message");
      msg = typeof msg === "string" ? msg : "";
      if (msg.length > 1500) msg = msg.slice(0, 1470) + "\n…(truncated)";

      var lines = [
        "Name: " + (fd.get("name") || ""),
        "Email: " + (fd.get("email") || ""),
        "Phone: " + (fd.get("phone") || ""),
        "",
        msg,
      ];
      window.location.href =
        "mailto:hello@prime-ai.com?subject=" +
        subject +
        "&body=" +
        encodeURIComponent(lines.join("\n"));
    });
  }

  function initNavDropdowns(mqMobile) {
    document.querySelectorAll("[data-nav-dropdown]").forEach(function (dd) {
      var toggle = dd.querySelector(".nav-dropdown-toggle");
      if (!toggle) return;

      toggle.addEventListener("click", function (e) {
        if (!mqMobile.matches) return;
        e.preventDefault();
        e.stopPropagation();
        var willOpen = !dd.classList.contains("is-open");
        document.querySelectorAll("[data-nav-dropdown].is-open").forEach(
          function (other) {
            if (other !== dd) {
              other.classList.remove("is-open");
              var tb = other.querySelector(".nav-dropdown-toggle");
              if (tb) tb.setAttribute("aria-expanded", "false");
            }
          }
        );
        dd.classList.toggle("is-open", willOpen);
        toggle.setAttribute("aria-expanded", willOpen ? "true" : "false");
      });
    });

    window.addEventListener("resize", function () {
      if (!mqMobile.matches) closeAllNavDropdowns();
    });
  }

  function initStickyCta() {
    var el = document.getElementById("sticky-cta");
    if (!el) return;

    var cur = pathnameFile().toLowerCase();
    if (cur === "contact.html") {
      el.setAttribute("hidden", "");
      return;
    }

    var showAfter = 340;
    var ticking = false;

    function update() {
      ticking = false;
      var y = window.scrollY || window.pageYOffset;
      var docH = document.documentElement.scrollHeight;
      var winH = window.innerHeight;
      var nearBottom = y + winH > docH - 100;

      if (y > showAfter && !nearBottom) el.removeAttribute("hidden");
      else el.setAttribute("hidden", "");
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

  function initMobileNav() {
    var wrap = document.querySelector(".pill-nav-wrap");
    var toggle = document.querySelector(".nav-toggle");
    var sheet = document.getElementById("site-nav-sheet");
    var overlay = document.querySelector(".nav-overlay");
    if (!wrap || !toggle || !sheet) return;

    var mqMobile = window.matchMedia("(max-width: 860px)");

    function syncSheetAria() {
      var mobile = mqMobile.matches;
      var open = wrap.classList.contains("is-nav-open");
      if (!mobile) {
        sheet.removeAttribute("aria-hidden");
        sheet.removeAttribute("inert");
        if (overlay) overlay.setAttribute("aria-hidden", "true");
        return;
      }
      sheet.setAttribute("aria-hidden", open ? "false" : "true");
      if (overlay) overlay.setAttribute("aria-hidden", open ? "false" : "true");
      if (open) sheet.removeAttribute("inert");
      else sheet.setAttribute("inert", "");
    }

    function setOpen(open) {
      var mobile = mqMobile.matches;
      if (!mobile) {
        wrap.classList.remove("is-nav-open");
        toggle.setAttribute("aria-expanded", "false");
        document.documentElement.style.overflow = "";
        closeAllNavDropdowns();
        syncSheetAria();
        return;
      }
      wrap.classList.toggle("is-nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.documentElement.style.overflow = open ? "hidden" : "";
      if (!open) closeAllNavDropdowns();
      syncSheetAria();
    }

    initNavDropdowns(mqMobile);

    toggle.addEventListener("click", function () {
      if (!mqMobile.matches) return;
      setOpen(!wrap.classList.contains("is-nav-open"));
    });

    if (overlay) {
      overlay.addEventListener("click", function () {
        setOpen(false);
      });
    }

    sheet.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        if (mqMobile.matches) setOpen(false);
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && wrap.classList.contains("is-nav-open")) {
        setOpen(false);
        toggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      syncSheetAria();
      if (!mqMobile.matches) {
        wrap.classList.remove("is-nav-open");
        toggle.setAttribute("aria-expanded", "false");
        document.documentElement.style.overflow = "";
      }
    });

    syncSheetAria();
  }

  function initAll() {
    setNavActiveByPathname();
    initMobileNav();
    initStickyCta();
    initDiscoveryForm();
    initContactFormAlias();

    window.addEventListener("load", function () {
      setNavActiveByPathname();
    });

    window.addEventListener(
      "popstate",
      function () {
        setNavActiveByPathname();
      },
      false
    );

    window.addEventListener(
      "hashchange",
      function () {
        setNavActiveByPathname();
      },
      false
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
})();
