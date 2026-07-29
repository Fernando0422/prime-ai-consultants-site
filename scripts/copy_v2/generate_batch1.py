#!/usr/bin/env python3
"""Generate legally conservative copy v2.0 pages."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shell import page, BUSINESS_EMAIL, PRIVACY_EMAIL, EFFECTIVE_DATE, LINKEDIN_HREF, FORM_PROCESSOR, HOSTING_PROVIDER

ROOT = Path(__file__).resolve().parents[2]


def write(name, html):
    path = ROOT / name
    path.write_text(html, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


# ---------- HOME ----------
HOME_MAIN = r"""
    <section class="hero">
      <div class="hero-bg" aria-hidden="true">
        <div class="hero-bg-mesh"></div>
        <div class="hero-bg-vignette"></div>
      </div>
      <div class="container hero-inner">
        <div class="hero-copy">
          <span class="eyebrow">Operational AI for complex systems</span>
          <h1 class="h-display">AI cannot understand what your organization has never made explicit.</h1>
          <p class="lede">Prime AI works with operational teams to map the systems, business rules, and institutional knowledge that must be understood before AI or advanced analytics can be evaluated responsibly. Our experience is rooted in manufacturing and enterprise applications.</p>
          <div class="cta-row">
            <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your operational environment</a>
            <a href="methodology.html" class="btn btn-secondary btn-lg">See how we work</a>
          </div>
          <p class="hero-reassure">Founder-led. Vendor-neutral. Every engagement begins with a focused discovery conversation.</p>
        </div>
        <div class="hero-diagram" aria-label="Operational context diagram">
          <ul class="hero-diagram-list" role="list">
            <li>Operational systems</li>
            <li>Reports and calculations</li>
            <li>Business rules</li>
            <li>Expert knowledge</li>
            <li>Approved access paths</li>
            <li>Traceable analysis</li>
            <li>AI and analytics evaluated against operational context</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section-white home-section" aria-labelledby="problem-heading">
      <div class="container">
        <div class="section-head section-head-left measure-editorial">
          <span class="eyebrow">The problem beneath the pilot</span>
          <h2 class="h-h2" id="problem-heading">Most operational AI problems begin before the model.</h2>
          <p class="lede">Operational data may be abundant, but its meaning is rarely contained in one place. Definitions, calculations, exceptions, and accepted practices become distributed across databases, reports, application logic, spreadsheets, and the people who know how to interpret them.</p>
        </div>
        <ol class="signal-list">
          <li>
            <h3 class="signal-title">Important relationships are undocumented.</h3>
            <p>Tables may contain relevant information without clearly showing how the operation connects across orders, equipment, materials, quality, and time.</p>
          </li>
          <li>
            <h3 class="signal-title">Reports use competing definitions.</h3>
            <p>Two teams can calculate the same metric differently and both believe they are using the authoritative version.</p>
          </li>
          <li>
            <h3 class="signal-title">Business logic lives outside obvious tables.</h3>
            <p>The answer may depend on stored procedures, scheduled jobs, report formulas, application code, integrations, or manual conventions.</p>
          </li>
          <li>
            <h3 class="signal-title">Experienced employees remain the translators.</h3>
            <p>Critical context often lives in the judgment of a small number of people who know which source to use and when an exception changes the meaning.</p>
          </li>
        </ol>
        <div class="measure-editorial reframe-block">
          <p class="reframe-closing"><strong>The issue is not that a model cannot read the database. The issue is that the database does not explain the operation.</strong></p>
          <p>When operational meaning becomes explicit, teams can investigate questions more consistently, preserve critical knowledge, and evaluate new capabilities on a foundation they understand.</p>
        </div>
      </div>
    </section>

    <section class="section section-mist home-section" aria-labelledby="why-prime-heading">
      <div class="container">
        <div class="section-head section-head-left measure-editorial">
          <span class="eyebrow">Why Prime</span>
          <h2 class="h-h2" id="why-prime-heading">Two generations of enterprise technology.</h2>
          <p class="lede">Prime AI was built around a simple observation: modern AI initiatives often collide with decades of operational complexity that was never designed for machine interpretation.</p>
        </div>
        <div class="founder-split">
          <article class="founder-card">
            <img src="assets/founder-antonio.png" alt="Antonio Rojas, Co-Founder — Operational Systems" width="500" height="500" loading="lazy" decoding="async" />
            <h3 class="h-h3">Antonio Rojas</h3>
            <p class="founder-role">Co-Founder — Operational Systems</p>
            <p>Antonio Rojas has worked in enterprise applications and information technology for more than three decades. Since 2007, his professional experience has included applications leadership in semiconductor manufacturing, with public experience spanning SAP, Infor/Mapics, Oracle, systems integration, and cross-border initiatives. At Prime, he leads operational discovery, system analysis, business-logic reconstruction, and technical standards.</p>
          </article>
          <article class="founder-card">
            <img src="assets/founder-fernando.png" alt="Fernando Rojas, Co-Founder — Strategy and Service Design" width="500" height="500" loading="lazy" decoding="async" />
            <h3 class="h-h3">Fernando Rojas</h3>
            <p class="founder-role">Co-Founder — Strategy and Service Design</p>
            <p>Fernando Rojas leads company strategy, service design, client experience, market research, and the development of Prime’s delivery systems. His role is to translate operational expertise into a clear, modern, and disciplined client experience.</p>
          </article>
        </div>
        <div class="measure-editorial">
          <p>Prime is early as a firm. Its perspective comes from real enterprise environments, complementary founder roles, and a commitment to claim only what can be supported.</p>
          <p class="scope-notice">Our experience is rooted in manufacturing. We selectively consider other organizations whose critical decisions depend on complex operational systems.</p>
          <div class="cta-row">
            <a href="company.html" class="btn btn-primary">Meet the founders</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-dark home-section" aria-labelledby="method-heading">
      <div class="container">
        <div class="section-head section-head-left measure-editorial">
          <span class="eyebrow">The Prime approach</span>
          <h2 class="h-h2" id="method-heading">A structured path from operational complexity to a documented next step.</h2>
          <p class="lede">We begin with the system and the decision the organization needs to improve. We then recover meaning, define appropriate controls, and determine what a responsible next step would require.</p>
        </div>
        <ol class="process-steps process-steps--four">
          <li>
            <h3>Discover</h3>
            <p>Understand the systems, owners, dependencies, current reports, available evidence, and priority business question.</p>
          </li>
          <li>
            <h3>Define</h3>
            <p>Recover the relationships, calculations, terminology, exceptions, and operational meaning behind the selected use case.</p>
          </li>
          <li>
            <h3>Govern</h3>
            <p>Clarify proposed access paths, ownership, validation responsibilities, traceability, restrictions, and limits for client review.</p>
          </li>
          <li>
            <h3>Activate</h3>
            <p>Define the pilot, data surface, analysis workflow, or next investment around documented context.</p>
          </li>
        </ol>
        <p class="scope-notice scope-notice--dark measure-editorial">Activities, timing, and outputs vary by environment. The framework is a structured starting point, not a representation that every engagement is identical.</p>
        <div class="cta-row">
          <a href="methodology.html" class="btn btn-primary">Explore the methodology</a>
        </div>
      </div>
    </section>

    <section class="section section-white home-section" aria-labelledby="diagnostics-heading">
      <div class="container">
        <div class="section-head section-head-left measure-editorial">
          <span class="eyebrow">A focused starting point</span>
          <h2 class="h-h2" id="diagnostics-heading">Start with one system, one operational domain, and one decision.</h2>
          <p class="lede">Prime Diagnostics is a focused discovery and readiness engagement for organizations considering an operational AI or analytics initiative. We examine the selected system, the business meaning behind it, and the controls that would require client review before an implementation proceeds.</p>
        </div>
        <div class="two-col-editorial">
          <div>
            <h3 class="h-h3">Designed to clarify</h3>
            <ul class="check-list">
              <li>What data and logic are relevant to the selected question</li>
              <li>Which definitions appear established and which require validation</li>
              <li>Where important knowledge remains undocumented</li>
              <li>Where access may be appropriate and where additional review is required</li>
              <li>What ownership, controls, and validation a first pilot would require</li>
            </ul>
          </div>
          <div>
            <h3 class="h-h3">Possible outputs</h3>
            <ul class="check-list">
              <li>In-scope system inventory</li>
              <li>Priority relationship map</li>
              <li>Initial operational data dictionary</li>
              <li>Business-logic register</li>
              <li>Governance and readiness findings</li>
              <li>Prioritized next-step roadmap</li>
            </ul>
          </div>
        </div>
        <div class="measure-editorial">
          <p class="scope-notice">Final scope is agreed after an initial discovery conversation and documented in a written statement of work. Not every environment will require—or be suitable for—the same activities or outputs.</p>
          <p class="scope-notice">Clients receive editable, client-specific engagement outputs. Ownership and licensing terms are defined in the engagement agreement.</p>
          <div class="cta-row">
            <a href="contact.html?interest=diagnostics" class="btn btn-primary btn-arrow">Discuss Prime Diagnostics</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="home-final-cta">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="home-final-cta">Before you connect AI to operational data, make sure the organization understands it.</h2>
        <p class="lede">Tell us which system you are working with, what question your team needs to answer, and what is currently blocking progress. If you are not evaluating a project today but would like to stay connected as Prime develops, we would still be glad to hear from you.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your environment</a>
          <a href="__LINKEDIN__" class="btn btn-secondary btn-lg" data-fernando-linkedin>Connect with Fernando on LinkedIn</a>
        </div>
        <p class="response-note">We review every inquiry personally and aim to respond within one business day.</p>
      </div>
    </section>
""".replace("__LINKEDIN__", LINKEDIN_HREF)


# ---------- DIAGNOSTICS ----------
DIAG_MAIN = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Prime Diagnostics</span>
        <h1 class="h-h1">Understand the system before you build on it.</h1>
        <p class="lede lede-text">Prime Diagnostics is a focused discovery and readiness engagement for organizations considering an operational AI or analytics initiative. We examine one operational system, one priority domain, and one decision the organization needs to improve.</p>
        <div class="cta-row">
          <a href="contact.html?interest=diagnostics" class="btn btn-primary btn-arrow">Request a Diagnostics conversation</a>
          <a href="#coverage" class="btn btn-secondary">Review what the engagement covers</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="why-diag">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="why-diag">A roadmap is useful only when it is grounded in how the operation actually works.</h2>
        <p>Many teams already know their data is complicated. What they often do not have is a shared, documented view of which sources matter, how critical metrics are calculated, where exceptions live, who owns the definitions, and what access an AI system might require.</p>
        <p>Prime Diagnostics is designed to turn those unknowns into a bounded set of findings, open questions, and decisions before a larger implementation begins.</p>
      </div>
    </section>

    <section class="section section-mist" id="coverage" aria-labelledby="scope-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="scope-heading">One system. One domain. One decision.</h2>
        </div>
        <div class="definition-grid">
          <article>
            <h3 class="h-h3">System</h3>
            <p>A defined MES, ERP environment, CRM environment, custom operational application, database, or closely related set of sources.</p>
          </article>
          <article>
            <h3 class="h-h3">Domain</h3>
            <p>A bounded operational area such as yield, quality, downtime, work in progress, inventory, order fulfillment, production reporting, service operations, or customer operations.</p>
          </article>
          <article>
            <h3 class="h-h3">Decision</h3>
            <p>A specific question, investigation, reporting problem, or proposed AI use case that gives the engagement a clear purpose.</p>
          </article>
        </div>
        <p class="scope-notice measure-editorial">Broader environments can be divided into additional phases. Prime does not represent a focused diagnostic as a complete enterprise-wide data audit.</p>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="questions-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="questions-heading">Questions the engagement is designed to answer</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Which systems and data objects are relevant to the selected decision?</li>
          <li>Where do important relationships, calculations, and exceptions live?</li>
          <li>Which definitions appear established, and which still require an owner or validation?</li>
          <li>Which data surfaces may be appropriate for further evaluation?</li>
          <li>Which information should remain restricted pending legal, privacy, security, compliance, data-owner, or system-owner review?</li>
          <li>What would a credible pilot or next phase require?</li>
        </ul>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="outputs-heading">
      <div class="container">
        <div class="section-head section-head-left measure-editorial">
          <h2 class="h-h2" id="outputs-heading">Practical working materials, not a generic strategy deck.</h2>
        </div>
        <div class="deliverable-grid">
          <article><h3 class="h-h3">System inventory</h3><p>A structured view of in-scope databases, tables, views, procedures, reports, interfaces, and known owners relevant to the selected question.</p></article>
          <article><h3 class="h-h3">Priority relationship map</h3><p>A visual representation of how the most important entities, data flows, and system boundaries connect.</p></article>
          <article><h3 class="h-h3">Initial operational data dictionary</h3><p>A first-pass record of business meaning, source, ownership, sensitivity, relationships, confidence, and open questions for priority data objects.</p></article>
          <article><h3 class="h-h3">Business-logic register</h3><p>A record of important calculations, transformations, schedules, report rules, application behavior, and expert practices identified during the engagement.</p></article>
          <article><h3 class="h-h3">Governance and readiness findings</h3><p>Findings related to proposed access paths, validation responsibilities, traceability, restrictions, unresolved assumptions, and readiness for the selected use case.</p></article>
          <article><h3 class="h-h3">Prioritized roadmap</h3><p>Recommended next steps organized by what should be resolved first, what may be suitable for further evaluation, and what should not move forward yet.</p></article>
        </div>
        <p class="scope-notice measure-editorial">The final output set is determined by scope. These examples do not represent a universal promise that every engagement will require all listed materials.</p>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="process-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="process-heading">A structured discovery process, adapted to the environment.</h2>
        </div>
        <ol class="process-steps process-steps--five">
          <li><h3>Align</h3><p>Confirm the decision, scope, stakeholders, constraints, evidence available, and success criteria.</p></li>
          <li><h3>Examine</h3><p>Review available metadata, documentation, reports, logic, and system relationships using client-approved access.</p></li>
          <li><h3>Interpret</h3><p>Compare technical structure with operational meaning through interviews and evidence review.</p></li>
          <li><h3>Assess</h3><p>Document uncertainties, access considerations, validation needs, restrictions, and readiness for the selected use case.</p></li>
          <li><h3>Recommend</h3><p>Present findings, decisions required, and a practical next-step roadmap.</p></li>
        </ol>
        <p class="scope-notice measure-editorial">Timing depends on scope, access, system complexity, and stakeholder availability. A schedule is proposed only after the initial discovery conversation.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="participation-heading">
      <div class="container two-col-editorial">
        <div>
          <h2 class="h-h2" id="participation-heading">Client participation</h2>
          <ul class="check-list">
            <li>An accountable sponsor or decision-maker</li>
            <li>A technical owner for the selected system</li>
            <li>Available subject-matter experts</li>
            <li>Client-approved read-only access or a suitable representative environment</li>
            <li>Existing reports, documentation, and known problem examples</li>
            <li>Security, privacy, confidentiality, and governance requirements</li>
            <li>A clearly defined operational question</li>
          </ul>
        </div>
        <div>
          <h2 class="h-h2">Not included by default</h2>
          <ul class="check-list">
            <li>Production AI deployment</li>
            <li>Formal cybersecurity, privacy, legal, regulatory, financial, or compliance certification</li>
            <li>Full enterprise-wide schema documentation</li>
            <li>Remediation of every source-data issue</li>
            <li>Replacement of core systems</li>
            <li>Validation of every organizational KPI</li>
            <li>Guaranteed financial or operational outcomes</li>
            <li>Autonomous decision-making recommendations without client review</li>
          </ul>
        </div>
      </div>
      <div class="container">
        <p class="scope-notice scope-notice--emphasis measure-editorial">Prime’s recommendations do not replace review by the client’s legal, privacy, information-security, compliance, data-owner, system-owner, or executive functions. Final access and deployment decisions remain with the client.</p>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="fit-heading">
      <div class="container">
        <h2 class="h-h2 sr-only" id="fit-heading">Fit</h2>
        <div class="fit-block">
          <article>
            <h3 class="h-h3">Strong fit</h3>
            <p>An organization with a real operational system, a meaningful question, an identified owner, available experts, and willingness to examine the underlying context before implementation.</p>
          </article>
          <article>
            <h3 class="h-h3">Probably not a fit</h3>
            <p>A generic marketing chatbot, consumer application, request for a rapid demo without access controls, or project without an available system owner or operational question.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="diag-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="diag-final">Bring us the system and the question you need to understand.</h2>
        <p class="lede">We will use the first conversation to determine whether a focused diagnostic is appropriate, what information would be required, and whether Prime is the right fit.</p>
        <div class="cta-row">
          <a href="contact.html?interest=diagnostics" class="btn btn-primary btn-lg btn-arrow">Request a Diagnostics conversation</a>
        </div>
      </div>
    </section>
"""


write(
    "index.html",
    page(
        "Prime AI Consultants | Operational Systems Before AI",
        "Prime AI helps organizations understand the systems, business rules, and operational knowledge behind an AI or analytics initiative before implementation begins. Manufacturing-rooted. Founder-led.",
        "page-home page-site",
        "/",
        "home",
        HOME_MAIN,
    ),
)

write(
    "diagnostics.html",
    page(
        "Prime Diagnostics | Operational AI Discovery and Readiness",
        "A focused discovery and readiness engagement for one operational system, one priority domain, and one decision. Clarify data, business rules, access considerations, and next steps before implementation.",
        "page-route page-site page-diagnostics",
        "/diagnostics",
        "diagnostics",
        DIAG_MAIN,
    ),
)

print("batch1 done")
