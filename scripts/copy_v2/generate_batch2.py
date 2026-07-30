#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shell import page, BUSINESS_EMAIL, LINKEDIN_HREF

ROOT = Path(__file__).resolve().parents[2]

def write(name, html):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

METHOD_MAIN = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Our delivery framework</span>
        <h1 class="h-h1">From operational complexity to a documented next step.</h1>
        <p class="lede lede-text">Prime’s methodology is designed to uncover the technical structure, business meaning, ownership, and controls behind a selected operational question. The framework is informed by enterprise applications experience and will be refined as Prime completes engagements.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-arrow">Discuss your environment</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="premise-heading">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="premise-heading">Intelligence is impossible without context.</h2>
        <p>A model can retrieve a value without understanding why it matters, which calculation produced it, which exception changes its meaning, or who is accountable for validating it.</p>
        <p>Our methodology begins before implementation. It makes the relevant context visible enough for people to inspect, challenge, govern, and use in a deliberate next step.</p>
      </div>
    </section>

    <section class="section section-dark" aria-labelledby="stages-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="stages-heading">Four stages</h2>
        </div>
        <ol class="process-steps process-steps--four">
          <li><h3>Discover</h3><p>Understand the environment, system, stakeholders, evidence, and decision the organization needs to improve.</p></li>
          <li><h3>Define</h3><p>Recover the relationships, terms, calculations, exceptions, and operational meaning behind the selected use case.</p></li>
          <li><h3>Govern</h3><p>Clarify proposed access paths, ownership, validation responsibilities, traceability, restrictions, and unresolved risks for client review.</p></li>
          <li><h3>Activate</h3><p>Define and, when separately agreed in writing, implement the pilot, data surface, workflow, or intelligence layer around documented context.</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-mist" id="framework" aria-labelledby="phases-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="phases-heading">Detailed ten-phase framework</h2>
        </div>
        <div class="phase-detail-list phase-detail-list--accordion" role="list">
"""

phases = [
    ("1", "Executive alignment", "Confirm the decision, business purpose, accountable sponsor, scope, constraints, and standards for a useful outcome."),
    ("2", "System and stakeholder inventory", "Identify relevant systems, applications, reports, owners, users, subject-matter experts, and dependencies."),
    ("3", "Metadata and structure review", "Examine available schemas, tables, views, procedures, interfaces, jobs, reports, and documentation within the approved scope."),
    ("4", "Relationship and lineage analysis", "Trace important entities, dependencies, transformations, and information flows related to the selected question."),
    ("5", "Business meaning discovery", "Document terminology, calculations, exceptions, accepted practices, ownership, and areas where teams interpret the same data differently."),
    ("6", "Validation and confidence review", "Compare technical findings with reports, examples, and subject-matter expertise. Mark items as confirmed, inferred, unresolved, or restricted."),
    ("7", "Access and governance design", "Propose data surfaces, permissions, review responsibilities, logging, traceability, restrictions, and validation gates for client consideration."),
    ("8", "Pilot or workflow definition", "Define the bounded question, user, data surface, output, escalation path, and acceptance criteria for a possible next step."),
    ("9", "Implementation or handoff", "When separately scoped, create the agreed data surface, documentation, workflow, prototype, or implementation plan and hand over client-specific materials."),
    ("10", "Review and iteration", "Evaluate what was learned, document unresolved items, and recommend whether to expand, revise, pause, or discontinue the initiative."),
]

for num, title, body in phases:
    pid = f"phase-{num}"
    METHOD_MAIN += f"""
          <article class="phase-detail phase-detail--accordion" role="listitem">
            <h3 class="phase-detail-heading">
              <button type="button" class="phase-detail-trigger" aria-expanded="false" aria-controls="{pid}-panel" id="{pid}-btn">
                <span class="phase-num">Phase {num}</span>
                <span class="phase-title">{title}</span>
              </button>
            </h3>
            <div class="phase-detail-panel" id="{pid}-panel" role="region" aria-labelledby="{pid}-btn" hidden>
              <p>{body}</p>
            </div>
          </article>
"""

METHOD_MAIN += f"""
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="principles-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="principles-heading">Cross-cutting principles</h2>
        </div>
        <div class="deliverable-grid">
          <article><h3 class="h-h3">Evidence over assumption</h3><p>Separate confirmed facts, reasonable inferences, and unresolved questions.</p></article>
          <article><h3 class="h-h3">Human expertise remains part of the system</h3><p>Subject-matter experts validate meaning, exceptions, and acceptable use.</p></article>
          <article><h3 class="h-h3">Access is approved, bounded, and reviewable</h3><p>Production use should not rely on unrestricted access to raw operational tables without an access model approved by the client.</p></article>
          <article><h3 class="h-h3">Client decisions remain with the client</h3><p>Prime documents recommendations and tradeoffs. Legal, privacy, security, compliance, ownership, and deployment approvals remain with designated client functions.</p></article>
          <article><h3 class="h-h3">Client-specific outputs are portable</h3><p>Prime provides editable client-specific materials, subject to the ownership and licensing terms in the engagement agreement.</p></article>
        </div>
        <p class="scope-notice measure-editorial">The framework is not a universal ten-week promise. Activities can overlap, contract, expand, or stop depending on scope, evidence, access, risk, and decisions made during the engagement.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="arch-heading">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="arch-heading">Proposed access architecture</h2>
        <p>When an engagement reaches architecture discussion, Prime documents a proposed path that is subject to client review:</p>
        <ol class="check-list">
          <li>Operational source systems</li>
          <li>Client-approved read-only or representative access</li>
          <li>Documented definitions and logic</li>
          <li>Validation and ownership</li>
          <li>Proposed analysis, AI, or analytics surface</li>
        </ol>
        <p class="scope-notice">This architecture is proposed and subject to client technical, security, privacy, legal, and governance review. It is not a claim that every engagement will implement the same pattern.</p>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="method-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="method-final">Start with the system, the question, and the people who understand it.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your environment</a>
        </div>
      </div>
    </section>
"""

SERVICES_MAIN = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Services</span>
        <h1 class="h-h1">Understand first. Build deliberately.</h1>
        <p class="lede lede-text">Prime supports organizations that need to understand complex operational systems before committing to an AI or advanced-analytics implementation. Engagements are scoped around a defined system, question, decision, and set of client responsibilities.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-arrow">Discuss your environment</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="path-heading">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="path-heading">A staged path, not a mandatory package.</h2>
        <p>Some organizations need discovery before they can define a pilot. Others arrive with a documented environment and a narrower implementation question. Prime recommends only the stage that appears appropriate after an initial conversation.</p>
      </div>
    </section>

    <section class="section section-mist" id="diagnostics" aria-labelledby="svc-diag">
      <div class="container measure-editorial">
        <span class="eyebrow">Service 1 — Prime Diagnostics</span>
        <h2 class="h-h2" id="svc-diag">Discover what the system can support.</h2>
        <p>A focused engagement designed to document the relevant structure, meaning, ownership, access considerations, and open questions behind one operational decision or proposed use case.</p>
        <h3 class="h-h3">Possible activities</h3>
        <ul class="check-list">
          <li>Stakeholder and system discovery</li>
          <li>Metadata and documentation review</li>
          <li>Business-rule and definition interviews</li>
          <li>Relationship and logic mapping</li>
          <li>Access, restriction, and validation findings</li>
          <li>Next-step roadmap</li>
        </ul>
        <div class="cta-row">
          <a href="diagnostics.html" class="btn btn-primary">Explore Prime Diagnostics</a>
        </div>
      </div>
    </section>

    <section class="section section-white" id="architecture" aria-labelledby="svc-arch">
      <div class="container measure-editorial">
        <span class="eyebrow">Service 2 — Architecture and pilot definition</span>
        <h2 class="h-h2" id="svc-arch">Translate findings into a bounded technical plan.</h2>
        <p>Prime can help define a proposed data surface, validation model, workflow, pilot boundary, acceptance criteria, and implementation sequence. Final design decisions remain subject to client technical, security, privacy, legal, and governance review.</p>
        <h3 class="h-h3">Possible outputs</h3>
        <ul class="check-list">
          <li>Proposed architecture</li>
          <li>Approved-view or API recommendations</li>
          <li>Data and ownership requirements</li>
          <li>Pilot scope and acceptance criteria</li>
          <li>Validation and escalation model</li>
          <li>Implementation backlog</li>
        </ul>
      </div>
    </section>

    <section class="section section-mist" id="implementation" aria-labelledby="svc-impl">
      <div class="container measure-editorial">
        <span class="eyebrow">Service 3 — Implementation support</span>
        <h2 class="h-h2" id="svc-impl">Build only what has been understood and approved.</h2>
        <p>When separately agreed, Prime may support the creation of documentation, approved data views, integration patterns, prototypes, analysis workflows, or other client-specific implementation materials within the written scope.</p>
        <p class="scope-notice">Prime does not represent that every environment is suitable for AI, that every recommendation should proceed to production, or that implementation will produce a guaranteed financial or operational result.</p>
      </div>
    </section>

    <section class="section section-white" id="advisory" aria-labelledby="svc-adv">
      <div class="container measure-editorial">
        <span class="eyebrow">Service 4 — Ongoing advisory</span>
        <h2 class="h-h2" id="svc-adv">Extend the system without losing context.</h2>
        <p>After an initial engagement, Prime may provide separately scoped advisory support for documentation upkeep, new use-case review, governance decisions, architecture review, and knowledge transfer.</p>
        <p class="scope-notice">Ongoing support is offered only when appropriate and is defined in a separate agreement. No subscription or retainer is required to retain client-specific outputs already delivered.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="principles-svc">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="principles-svc">Working principles</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Vendor-neutral recommendations</li>
          <li>Read-only discovery where feasible</li>
          <li>Explicit assumptions and open questions</li>
          <li>Client-approved access</li>
          <li>Human validation</li>
          <li>Clear written scope</li>
          <li>Editable client-specific outputs</li>
        </ul>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="svc-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="svc-final">The first conversation is for defining the problem—not forcing a solution.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your environment</a>
        </div>
      </div>
    </section>
"""

COMPANY_MAIN = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Company</span>
        <h1 class="h-h1">Built to make complex systems easier to understand.</h1>
        <p class="lede lede-text">Prime AI is a founder-led consultancy developing a disciplined approach to operational AI and analytics readiness. We begin with the systems, definitions, business rules, and human knowledge that determine whether a proposed use case can be evaluated responsibly.</p>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="why-exists">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="why-exists">Technology changes faster than operational meaning becomes documented.</h2>
        <p>Organizations can invest in models, platforms, and interfaces while the context underneath remains fragmented. Prime exists to help make that context visible before a larger implementation begins.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="founder-story">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="founder-story">Two generations of enterprise technology.</h2>
        <p>Prime brings together Antonio Rojas’s long career in enterprise applications and information technology with Fernando Rojas’s work in strategy, service design, client experience, research, and company development. Their relationship is father and son; their professional roles are complementary.</p>
      </div>
    </section>

    <section class="section section-white team-section" aria-labelledby="founders-heading">
      <div class="container">
        <h2 class="sr-only" id="founders-heading">Founders</h2>
        <div class="team-list">
          <article class="team-member">
            <div class="team-photo">
              <img src="assets/founder-antonio.png" alt="Antonio Rojas, Co-Founder — Operational Systems" width="500" height="500" loading="lazy" decoding="async" />
            </div>
            <div class="team-copy">
              <h3 class="team-name">Antonio Rojas</h3>
              <p class="team-role">Co-Founder — Operational Systems</p>
              <div class="team-bio">
                <p>Antonio has worked in enterprise applications and information technology for more than three decades. Since 2007, his professional experience has included applications leadership in semiconductor manufacturing. His experience includes SAP, Infor/Mapics, Oracle, systems integration, and cross-border initiatives.</p>
                <p>At Prime, Antonio leads operational discovery, system analysis, business-logic reconstruction, technical review, and delivery standards.</p>
                <p class="scope-notice">Antonio’s employer experience is presented solely as professional background. Prime does not claim endorsement by his current or former employers, and does not use confidential employer information, data, systems, or outcomes in its marketing.</p>
              </div>
            </div>
          </article>
          <article class="team-member">
            <div class="team-photo">
              <img src="assets/founder-fernando.png" alt="Fernando Rojas, Co-Founder — Strategy and Service Design" width="500" height="500" loading="lazy" decoding="async" />
            </div>
            <div class="team-copy">
              <h3 class="team-name">Fernando Rojas</h3>
              <p class="team-role">Co-Founder — Strategy and Service Design</p>
              <div class="team-bio">
                <p>Fernando leads company strategy, service design, client experience, market research, brand communication, and the development of Prime’s delivery systems. His work focuses on translating operational expertise into clear services, useful client materials, and a disciplined company experience.</p>
                <p>Prime does not present Fernando as the sole technical authority for production AI systems. Technical recommendations are developed collaboratively and remain subject to client review and the written engagement scope.</p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="roles-heading">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="roles-heading">How the roles work together</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Antonio brings operational-systems judgment and enterprise applications experience.</li>
          <li>Fernando structures the service, research, communication, and client experience.</li>
          <li>Prime documents assumptions, unresolved questions, ownership, and limitations.</li>
          <li>Client legal, privacy, security, compliance, data-owner, and executive functions retain final decision authority.</li>
        </ul>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="principles-co">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="principles-co">Principles</h2>
        </div>
        <div class="deliverable-grid">
          <article><h3 class="h-h3">Context before implementation</h3><p>Understand the system and meaning before recommending a technical solution.</p></article>
          <article><h3 class="h-h3">Evidence before claims</h3><p>Distinguish confirmed facts, inferences, hypotheses, and unresolved questions.</p></article>
          <article><h3 class="h-h3">Governance by design</h3><p>Identify ownership, access, validation, and restrictions during discovery—not only after a prototype exists.</p></article>
          <article><h3 class="h-h3">Human expertise remains essential</h3><p>Operational experts help determine what the data means and how exceptions should be interpreted.</p></article>
          <article><h3 class="h-h3">Client-specific work stays usable</h3><p>Provide editable client-specific outputs under clearly written ownership and licensing terms.</p></article>
        </div>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="stage-heading">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="stage-heading">Prime is building carefully and in public.</h2>
        <p>Prime has not yet completed a paid client engagement under the Prime AI name. The firm is developing and refining its methodology, pursuing appropriate early engagements, and committing to update its public claims as evidence is earned.</p>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="co-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="co-final">A useful relationship can begin before a project does.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your environment</a>
          <a href="{LINKEDIN_HREF}" class="btn btn-secondary btn-lg" data-fernando-linkedin>Connect with Fernando on LinkedIn</a>
        </div>
      </div>
    </section>
"""

CONTACT_MAIN = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Contact</span>
        <h1 class="h-h1">Start with the system and the question.</h1>
        <p class="lede lede-text">Tell us what your organization is trying to understand, which system is involved, and what is currently blocking progress. We will review the inquiry and determine whether a conversation would be useful.</p>
      </div>
    </section>

    <section class="section section-mist home-section" id="inquiry">
      <div class="container">
        <div class="home-shell home-shell--pad contact-grid">
          <form
            id="contact-form"
            class="contact-form"
            action="https://formspree.io/f/xgoqorke"
            method="POST"
            novalidate
          >
            <input type="hidden" name="interest" id="interest-field" value="" />
            <label class="form-field">
              <span class="form-label">Name<span class="req">*</span></span>
              <input class="form-input" name="name" type="text" required autocomplete="name" aria-required="true" />
              <span class="form-error" data-error-for="name" hidden>Please complete this field.</span>
            </label>

            <label class="form-field">
              <span class="form-label">Work email<span class="req">*</span></span>
              <input class="form-input" name="email" type="email" required autocomplete="email" aria-required="true" />
              <span class="form-error" data-error-for="email" hidden>Enter a valid email address.</span>
            </label>

            <label class="form-field">
              <span class="form-label">Company<span class="req">*</span></span>
              <input class="form-input" name="company" type="text" required autocomplete="organization" aria-required="true" />
              <span class="form-error" data-error-for="company" hidden>Please complete this field.</span>
            </label>

            <label class="form-field">
              <span class="form-label">Role<span class="req">*</span></span>
              <input class="form-input" name="role" type="text" required autocomplete="organization-title" aria-required="true" />
              <span class="form-error" data-error-for="role" hidden>Please complete this field.</span>
            </label>

            <label class="form-field">
              <span class="form-label">Primary system</span>
              <input class="form-input" name="primarySystem" type="text" autocomplete="off" placeholder="MES, ERP, CRM, custom application, database, or not sure" />
            </label>

            <label class="form-field">
              <span class="form-label">What are you trying to understand or improve?<span class="req">*</span></span>
              <textarea
                class="form-textarea"
                name="message"
                required
                rows="5"
                aria-required="true"
                placeholder="Describe the operational question, reporting problem, or proposed AI or analytics use case. Please do not include passwords, production data, trade secrets, personal information, regulated information, security-sensitive details, or other confidential material."
              ></textarea>
              <span class="form-error" data-error-for="message" hidden>Please complete this field.</span>
            </label>

            <label class="form-field">
              <span class="form-label">Desired timeline</span>
              <select class="form-select" name="timeline">
                <option value="">Select timeline (optional)</option>
                <option value="exploring">Exploring</option>
                <option value="within-3-months">Within 3 months</option>
                <option value="within-6-months">Within 6 months</option>
                <option value="later">Later or not sure</option>
              </select>
            </label>

            <div class="form-notices">
              <p class="form-notice">Prime AI Consultants collects the information you submit to evaluate and respond to your inquiry, maintain business records, and protect the security of our website and communications. Please do not submit confidential, proprietary, regulated, or security-sensitive information. Review our <a href="privacy.html">Privacy Policy</a> for more information.</p>
              <p class="form-notice">Submitting this form does not create a client, advisory, fiduciary, or confidential relationship. Confidentiality obligations apply only after both parties sign an appropriate written agreement.</p>
            </div>

            <button type="submit" class="btn btn-primary btn-lg form-submit">Submit inquiry</button>
            <div class="form-status" role="status" aria-live="polite"></div>
            <div id="form-success" class="form-success" hidden>
              <h2 class="h-h2">Thank you. Your inquiry has been received.</h2>
              <p>We will review the information provided and aim to respond within one business day. Please do not send confidential or security-sensitive materials unless Prime has confirmed an appropriate secure process and the parties have signed the necessary agreement.</p>
              <a href="index.html" class="btn btn-primary">Return home</a>
            </div>
          </form>

          <aside class="contact-info" aria-label="What happens next">
            <div class="contact-info-block">
              <h2 class="contact-info-label" id="next-heading">We review every inquiry personally.</h2>
              <p>We aim to respond within one business day. An initial conversation is used to understand the environment, clarify whether Prime is a potential fit, and identify what additional information—if any—would be appropriate to discuss under an agreement.</p>
            </div>
            <div class="contact-info-block">
              <h3 class="contact-info-label">Alternate contact</h3>
              <ul class="contact-info-list">
                <li>Email: <a href="mailto:{BUSINESS_EMAIL}">{BUSINESS_EMAIL}</a></li>
                <li>LinkedIn: <a href="{LINKEDIN_HREF}" data-fernando-linkedin>Connect with Fernando Rojas</a></li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </section>
"""

write("methodology.html", page(
    "Methodology | Prime AI Consultants",
    "Discover, define, govern, and activate. Review Prime AI’s structured framework for understanding operational systems before an AI or analytics implementation.",
    "page-methodology page-site",
    "/methodology",
    "methodology",
    METHOD_MAIN,
    extra_fonts="&family=JetBrains+Mono:wght@400;500;600",
))
write("services.html", page(
    "Services | Prime AI Consultants",
    "Founder-led discovery, readiness, architecture, and implementation support for organizations evaluating AI and analytics in complex operational systems.",
    "page-route page-site",
    "/services",
    "services",
    SERVICES_MAIN,
))
write("company.html", page(
    "Company | Prime AI Consultants",
    "Meet the founders of Prime AI Consultants and learn why the firm begins with operational context, documented meaning, and disciplined claims.",
    "page-route page-site page-company",
    "/company",
    "company",
    COMPANY_MAIN,
))
write("contact.html", page(
    "Contact | Prime AI Consultants",
    "Tell Prime AI which operational system, question, or AI-readiness concern your organization is evaluating.",
    "page-route page-site",
    "/contact",
    "contact",
    CONTACT_MAIN,
))
print("batch2 done")
