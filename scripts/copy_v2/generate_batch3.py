#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shell import page, BUSINESS_EMAIL, PRIVACY_EMAIL, EFFECTIVE_DATE, FORM_PROCESSOR, HOSTING_PROVIDER

ROOT = Path(__file__).resolve().parents[2]

def write(name, html):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

MES = """
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">AI for MES</span>
        <h1 class="h-h1">MES data records the operation. It does not always explain it.</h1>
        <p class="lede lede-text">Manufacturing execution systems contain valuable operational history, but the meaning behind that history may be distributed across schemas, procedures, reports, integrations, configurations, and expert practice. Prime helps teams investigate that context before relying on AI or advanced analytics.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-arrow">Discuss your MES environment</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="mes-why">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="mes-why">The answer rarely lives in one table.</h2>
        <p>A question about yield, quality, downtime, work in progress, rework, or cycle time may depend on multiple systems, transformations, definitions, and exceptions. The correct interpretation can change by line, product, recipe, operation, shift, or reporting convention.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="mes-sources">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="mes-sources">Common sources of hidden meaning</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Stored procedures and scheduled jobs</li>
          <li>Report calculations</li>
          <li>Equipment and process integrations</li>
          <li>Status histories and event sequences</li>
          <li>Product, route, recipe, and operation definitions</li>
          <li>Manual adjustments and exception handling</li>
          <li>Tribal knowledge held by engineers, planners, analysts, and application owners</li>
        </ul>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="mes-questions">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="mes-questions">Questions a bounded engagement may investigate</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Which sources contribute to a selected production metric?</li>
          <li>Why do two trusted reports disagree?</li>
          <li>Which relationships are documented and which are inferred?</li>
          <li>Where are exceptions and rework represented?</li>
          <li>Which definitions require SME validation?</li>
          <li>What access path would require further client review before a pilot?</li>
        </ul>
      </div>
    </section>

    <section class="section section-dark" aria-labelledby="mes-approach">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="mes-approach">Prime’s approach</h2>
        </div>
        <ol class="process-steps process-steps--four">
          <li><h3>Discover</h3><p>Define the MES environment, stakeholders, reports, and operational question.</p></li>
          <li><h3>Define</h3><p>Trace relationships, calculations, status logic, exceptions, and business meaning.</p></li>
          <li><h3>Govern</h3><p>Document proposed access paths, ownership, restrictions, validation, and traceability for client review.</p></li>
          <li><h3>Activate</h3><p>Define a bounded pilot, data surface, workflow, or next-step roadmap.</p></li>
        </ol>
        <p class="scope-notice scope-notice--dark measure-editorial">Prime does not claim partnership with, certification by, or endorsement from any MES vendor unless expressly stated in writing. Product names may be used only to describe publicly verifiable professional experience or client-approved project context.</p>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="mes-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="mes-final">Begin with one manufacturing question the current system cannot answer consistently.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your MES environment</a>
        </div>
      </div>
    </section>
"""

ERP = """
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">AI for ERP</span>
        <h1 class="h-h1">Enterprise data becomes useful when its business meaning is explicit.</h1>
        <p class="lede lede-text">ERP systems connect finance, inventory, procurement, orders, production, and planning, but business meaning may be distributed across configurations, customizations, reports, integrations, and local practice. Prime helps teams investigate that context before evaluating an AI or analytics use case.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-arrow">Discuss your ERP environment</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="erp-challenge">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="erp-challenge">A system of record can still contain multiple versions of meaning.</h2>
        <p>A field may be technically defined while its operational use depends on configuration, custom logic, transaction timing, organizational policy, or an external spreadsheet. AI does not resolve those differences merely by receiving access.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="erp-questions">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="erp-questions">Common questions</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>Which system or report is authoritative for the selected decision?</li>
          <li>Where are important calculations and transformations performed?</li>
          <li>Which customizations change standard behavior?</li>
          <li>Which definitions differ across sites, teams, or business units?</li>
          <li>Which data requires additional privacy, security, legal, financial, or owner review?</li>
          <li>What would a bounded pilot need to document first?</li>
        </ul>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="erp-approach">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="erp-approach">Approach</h2>
        <p>Prime begins with a selected system, operational domain, and decision. We document relevant structure, meaning, ownership, access considerations, and unresolved questions before recommending a next step.</p>
        <p class="scope-notice">Prime is vendor-neutral and does not claim partnership, certification, or endorsement from ERP vendors unless expressly stated. References to SAP, Infor/Mapics, and Oracle describe Antonio Rojas’s professional experience, not Prime client engagements or vendor partnerships.</p>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="erp-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="erp-final">Bring us the ERP question your teams answer differently.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your ERP environment</a>
        </div>
      </div>
    </section>
"""

CRM = """
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">AI for CRM</span>
        <h1 class="h-h1">Customer data needs context before automation can use it responsibly.</h1>
        <p class="lede lede-text">CRM environments can combine customer records, sales activity, service history, workflow rules, notes, integrations, and sensitive information. Prime’s discovery framework can help an organization define the system, question, ownership, and controls that require review before an AI or analytics initiative proceeds.</p>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-arrow">Discuss your CRM environment</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="crm-warn">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="crm-warn">This is a selective application of Prime’s framework—not a claim of broad CRM delivery history.</h2>
        <p>Prime’s strongest experience is rooted in manufacturing and enterprise applications. We consider CRM-related work only when the problem depends on complex operational context and the required expertise, access, and client governance functions are available.</p>
      </div>
    </section>

    <section class="section section-mist" aria-labelledby="crm-questions">
      <div class="container">
        <div class="section-head section-head-left">
          <h2 class="h-h2" id="crm-questions">Questions to resolve first</h2>
        </div>
        <ul class="check-list measure-editorial">
          <li>What business decision or workflow is being considered?</li>
          <li>Which data is necessary for that purpose?</li>
          <li>Which fields contain personal, sensitive, confidential, or regulated information?</li>
          <li>Who owns the definitions and access decisions?</li>
          <li>What human review must remain in the workflow?</li>
          <li>Which uses should not proceed without additional legal, privacy, security, compliance, or customer review?</li>
        </ul>
        <p class="scope-notice measure-editorial">Prime does not provide privacy, employment, consumer-protection, credit, healthcare, or sector-specific legal advice. CRM use cases involving personal information require review by the client’s qualified legal, privacy, security, compliance, and data-owner functions.</p>
      </div>
    </section>

    <section class="section section-dark final-cta-section" aria-labelledby="crm-final">
      <div class="container measure-editorial">
        <h2 class="h-h2" id="crm-final">Start with the decision, the data required, and the people accountable for its use.</h2>
        <div class="cta-row">
          <a href="contact.html" class="btn btn-primary btn-lg btn-arrow">Discuss your CRM environment</a>
        </div>
      </div>
    </section>
"""

PRIVACY = f"""
    <section class="page-hero page-hero--short">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Legal</span>
        <h1 class="h-h1">Privacy Policy</h1>
        <p class="lede lede-text">Effective date: {EFFECTIVE_DATE}</p>
      </div>
    </section>

    <section class="section section-white legal-body">
      <div class="container measure-legal">
        <p>Prime AI Consultants LLC (“Prime,” “we,” “us,” or “our”) respects your privacy. This Privacy Policy explains the information we collect through this website, how we use and disclose it, and the choices available to you.</p>

        <h2>1. Information you provide</h2>
        <p>We may collect information you voluntarily provide, including:</p>
        <ul>
          <li>Name</li>
          <li>Work email address</li>
          <li>Company</li>
          <li>Role or job title</li>
          <li>Primary system or technology environment</li>
          <li>Project timing</li>
          <li>Information included in an inquiry or other communication</li>
        </ul>
        <p>Please do not submit passwords, production data, trade secrets, personal information relating to other people, regulated information, security-sensitive information, or other confidential material through the public contact form.</p>

        <h2>2. Information collected automatically</h2>
        <p>When you use the website, our hosting and related providers may automatically process technical information such as:</p>
        <ul>
          <li>IP address</li>
          <li>Browser and device type</li>
          <li>Operating system</li>
          <li>Referring page</li>
          <li>Pages viewed</li>
          <li>Date and time of access</li>
          <li>Approximate location derived from IP address</li>
          <li>Website performance, security, and interaction data</li>
        </ul>
        <p>As of the effective date, Prime does not use a separate analytics product on this website. Hosting is provided by {HOSTING_PROVIDER}. Contact-form submissions are processed by {FORM_PROCESSOR}.</p>

        <h2>3. How we use information</h2>
        <p>We may use information to:</p>
        <ul>
          <li>Evaluate and respond to inquiries</li>
          <li>Communicate about potential or existing business relationships</li>
          <li>Operate, secure, maintain, and improve the website</li>
          <li>Maintain appropriate business and legal records</li>
          <li>Prevent fraud, abuse, or security incidents</li>
          <li>Comply with legal obligations and protect rights</li>
        </ul>

        <h2>4. How we disclose information</h2>
        <p>We may disclose information to:</p>
        <ul>
          <li>Hosting, form-processing, email, security, and professional-service providers acting on our behalf</li>
          <li>Advisors, insurers, accountants, auditors, and legal counsel</li>
          <li>Government authorities or other parties when required by law or reasonably necessary to protect rights, safety, security, or the integrity of our services</li>
          <li>A successor or participant in a merger, acquisition, financing, reorganization, sale of assets, or similar transaction, subject to applicable law</li>
        </ul>
        <p>We do not disclose contact-form information for third-party direct marketing.</p>

        <h2>5. Sale and sharing</h2>
        <p>Prime does not sell personal information for money. The website does not currently use advertising, cross-context behavioral analytics, or retargeting pixels. If that changes, this Policy will be updated and any required choice mechanisms will be implemented.</p>

        <h2>6. Cookies and similar technologies</h2>
        <p>We do not intentionally use advertising cookies or cross-site tracking technologies. Our providers may use strictly necessary technologies to operate, secure, and deliver the website. Local storage may be used only for optional announcement-bar dismissal preferences on your device.</p>

        <h2>7. Retention</h2>
        <p>We retain information for as long as reasonably necessary for the purposes described in this Policy, including responding to inquiries, maintaining business records, resolving disputes, enforcing agreements, and complying with legal obligations. Retention periods vary according to the type of information, purpose, sensitivity, and applicable requirements.</p>

        <h2>8. Security</h2>
        <p>We use reasonable administrative, technical, and organizational measures designed to protect information. No method of transmission, storage, or security is guaranteed to be completely secure.</p>

        <h2>9. Your choices and requests</h2>
        <p>You may contact us to request access to, correction of, or deletion of information you have submitted, subject to applicable law and appropriate verification. You may also ask questions about our privacy practices.</p>
        <p>Email: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a></p>

        <h2>10. California residents</h2>
        <p>California law may provide eligible residents with rights regarding personal information, depending on whether Prime is subject to the applicable law and whether an exception applies. These rights may include requesting access, correction, or deletion and receiving information about collection, use, and disclosure.</p>
        <p>Prime will not discriminate against an individual for exercising an applicable privacy right. Requests may be submitted to <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>. Prime may need to verify a request and may deny or limit it where permitted by law.</p>
        <p>This section describes possible rights and does not claim that Prime is subject to the CCPA unless counsel confirms statutory thresholds and applicability.</p>

        <h2>11. Do Not Track and preference signals</h2>
        <p>Some browsers offer “Do Not Track” settings. Because there is no universally accepted response standard, the website may not respond to traditional Do Not Track signals.</p>
        <p>If Prime becomes subject to a law requiring recognition of browser-based opt-out preference signals, Prime will implement and describe the applicable process.</p>

        <h2>12. Children</h2>
        <p>This website is intended for business audiences and is not directed to children under 13. We do not knowingly collect personal information from children under 13 through this website. If you believe a child has submitted information, contact <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.</p>

        <h2>13. External links</h2>
        <p>The website may link to third-party services, including LinkedIn. Their privacy practices are governed by their own policies, not this Policy.</p>

        <h2>14. Changes</h2>
        <p>We may update this Policy to reflect changes in our practices, technologies, or legal obligations. The effective date above indicates when the Policy was last revised.</p>

        <h2>15. Contact</h2>
        <p>Prime AI Consultants LLC<br/>
        Email: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a></p>
        <p>A business mailing address will be published here when approved for public use.</p>
      </div>
    </section>
"""

TERMS = f"""
    <section class="page-hero page-hero--short">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Legal</span>
        <h1 class="h-h1">Terms of Use</h1>
        <p class="lede lede-text">Effective date: {EFFECTIVE_DATE}</p>
      </div>
    </section>

    <section class="section section-white legal-body">
      <div class="container measure-legal">
        <p>These Terms of Use govern your access to the Prime AI Consultants website. By using the website, you agree to these Terms. If you do not agree, do not use the website.</p>

        <h2>1. Informational purpose</h2>
        <p>Website content is provided for general informational and marketing purposes. It is not legal, regulatory, cybersecurity, financial, accounting, investment, employment, or other professional advice and should not be relied upon as a substitute for advice from qualified professionals.</p>

        <h2>2. No client or confidential relationship</h2>
        <p>Using the website, submitting a form, sending an email, or participating in an introductory conversation does not create a client, advisory, fiduciary, partnership, agency, employment, or confidential relationship. A consulting relationship and confidentiality obligations arise only through an appropriate written agreement signed by authorized representatives.</p>
        <p>Do not submit confidential, proprietary, regulated, personal, export-controlled, or security-sensitive information through the public website.</p>

        <h2>3. No guarantees</h2>
        <p>Prime does not guarantee that website information is complete, current, error-free, suitable for a particular purpose, or that any described framework, recommendation, service, or engagement will produce a particular technical, operational, financial, security, compliance, or business outcome.</p>

        <h2>4. Engagements require written agreements</h2>
        <p>All services are subject to evaluation, availability, conflict checks where appropriate, and a separate written agreement defining scope, fees, responsibilities, access, intellectual property, confidentiality, limitations, and other terms. Website descriptions are not offers capable of acceptance and do not create a commitment to perform services.</p>

        <h2>5. Intellectual property</h2>
        <p>The website and its original text, graphics, diagrams, trademarks, logos, frameworks, and other materials are owned by or licensed to Prime and are protected by applicable laws. You may view and print reasonable portions for internal, noncommercial evaluation. You may not reproduce, distribute, modify, publish, sell, scrape, train models on, or create derivative works from website content except as permitted by law or with written permission.</p>

        <h2>6. Third-party names and links</h2>
        <p>Third-party product and company names may be trademarks of their respective owners. References do not imply affiliation, certification, partnership, sponsorship, or endorsement unless expressly stated.</p>
        <p>The website may contain links to third-party services. Prime is not responsible for their content, availability, security, or privacy practices.</p>

        <h2>7. Prohibited use</h2>
        <p>You may not:</p>
        <ul>
          <li>Use the website unlawfully or to violate another person’s rights</li>
          <li>Attempt unauthorized access, interference, disruption, scraping, probing, or circumvention of security controls</li>
          <li>Introduce malicious code</li>
          <li>Misrepresent affiliation with Prime</li>
          <li>Use website content in a misleading or deceptive manner</li>
        </ul>

        <h2>8. Disclaimer</h2>
        <p>To the maximum extent permitted by law, the website is provided “as is” and “as available,” without warranties of any kind, whether express, implied, or statutory, including implied warranties of merchantability, fitness for a particular purpose, title, and non-infringement.</p>

        <h2>9. Limitation of liability</h2>
        <p>To the maximum extent permitted by law, Prime and its members, managers, employees, contractors, and representatives will not be liable for indirect, incidental, special, consequential, exemplary, or punitive damages arising from or related to use of, or inability to use, the website.</p>
        <p class="scope-notice">Liability limitations vary by jurisdiction and should be reviewed by counsel before publication. This clause does not govern paid consulting engagements; engagement agreements require separate limitations.</p>

        <h2>10. Indemnity</h2>
        <p>You agree to be responsible for losses arising from your unlawful misuse of the website or violation of these Terms, to the extent permitted by applicable law.</p>
        <p class="scope-notice">Counsel should confirm whether this clause is appropriate for the public website.</p>

        <h2>11. Governing law</h2>
        <p>These Terms are governed by the laws of the State of California, without regard to conflict-of-laws principles. Venue will lie in the state or federal courts located in California, subject to applicable law.</p>
        <p class="scope-notice">Counsel should confirm county, venue, and enforceability before publication. A specific county has not yet been designated.</p>

        <h2>12. Changes</h2>
        <p>Prime may update these Terms. The effective date indicates the latest revision. Continued use after a change constitutes acceptance to the extent permitted by law.</p>

        <h2>13. Contact</h2>
        <p>Email: <a href="mailto:{BUSINESS_EMAIL}">{BUSINESS_EMAIL}</a></p>
      </div>
    </section>
"""

A11Y = f"""
    <section class="page-hero page-hero--short">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Accessibility</span>
        <h1 class="h-h1">Accessibility statement</h1>
      </div>
    </section>

    <section class="section section-white legal-body">
      <div class="container measure-legal">
        <p>Prime AI Consultants is committed to providing a website that is usable by as many people as reasonably possible, including people with disabilities.</p>
        <p>We are working to support recognized accessibility practices, including:</p>
        <ul>
          <li>Semantic headings and landmarks</li>
          <li>Keyboard-accessible navigation and forms</li>
          <li>Visible focus indicators</li>
          <li>Sufficient color contrast</li>
          <li>Text alternatives for meaningful images</li>
          <li>Form labels and understandable error messages</li>
          <li>Reduced-motion preferences</li>
          <li>Responsive layouts and browser zoom</li>
        </ul>
        <p>Accessibility is an ongoing process. If you experience difficulty using the website or accessing information, contact us at <a href="mailto:{BUSINESS_EMAIL}">{BUSINESS_EMAIL}</a> and identify the page, feature, and assistance needed. We will make reasonable efforts to provide the information through an accessible alternative and improve the experience.</p>
        <p>This statement does not claim conformance that has not been tested. After formal testing, Prime may state a specific target such as WCAG 2.2 Level AA only if the implementation and test record support that statement.</p>
      </div>
    </section>
"""

NOT_FOUND = f"""
    <section class="page-hero">
      <div class="container page-hero-inner">
        <span class="eyebrow hero-eyebrow">Page not found</span>
        <h1 class="h-h1">This page is not part of the current system.</h1>
        <p class="lede lede-text">The address may be outdated, or the page may have moved as Prime’s website has evolved.</p>
        <div class="cta-row">
          <a href="index.html" class="btn btn-primary btn-arrow">Return home</a>
          <a href="contact.html" class="btn btn-secondary">Contact Prime</a>
        </div>
      </div>
    </section>
"""

write("ai-mes.html", page("AI for MES | Prime AI Consultants", "Understand MES data, business rules, relationships, and access considerations before evaluating an AI or advanced-analytics use case in manufacturing.", "page-route page-site", "/ai-mes", "", MES))
write("ai-erp.html", page("AI for ERP | Prime AI Consultants", "Clarify ERP data, calculations, ownership, and access considerations before evaluating AI or advanced analytics across operational workflows.", "page-route page-site", "/ai-erp", "", ERP))
write("ai-crm.html", page("AI for CRM | Prime AI Consultants", "Clarify customer, service, workflow, and ownership context before evaluating AI or analytics in a CRM or related operational system.", "page-route page-site", "/ai-crm", "", CRM))
write("privacy.html", page("Privacy Policy | Prime AI Consultants", "Privacy Policy for the Prime AI Consultants website.", "page-route page-site", "/privacy", "", PRIVACY))
write("terms.html", page("Terms of Use | Prime AI Consultants", "Terms of Use for the Prime AI Consultants website.", "page-route page-site", "/terms", "", TERMS))
write("accessibility.html", page("Accessibility | Prime AI Consultants", "Accessibility statement for the Prime AI Consultants website.", "page-route page-site", "/accessibility", "", A11Y))
write("404.html", page("Page not found | Prime AI Consultants", "The requested page is not part of the current Prime AI Consultants website.", "page-route page-site", "/404", "", NOT_FOUND))
print("batch3 done")
