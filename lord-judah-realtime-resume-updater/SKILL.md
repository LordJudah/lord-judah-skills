---
name: lord-judah-realtime-resume-updater
description: Produce and maintain evidence-based, role-tailored résumés for Cornell “Lord Judah” Carelock. Use when preparing a résumé, CV, or application materials; refreshing professional credentials; searching authorized email or project files for recent accomplishments; or tailoring career materials to arts education, advocacy, community engagement, teaching artist, creative leadership, or related roles.
---

# Lord Judah Real-Time Résumé Updater

Create an application-specific résumé that reflects Cornell “Lord Judah” Carelock’s latest **verified** experience, credentials, leadership roles, and professional learning at the time of use. Treat each run as a fresh evidence-gathering pass; never assume an earlier résumé is current.

## Core Rule

> A résumé is current only to the last verified source check. Do not claim that it is “real-time” in an absolute sense; label it **Updated through [date/time and sources searched]** when a dated record is needed.

## Required Inputs

Collect or infer the following before drafting:

1. Target role, organization, job posting, and deadline.
2. Desired output: PDF résumé, source document, CV, or application packet.
3. Authorized sources to search. Default to project shared files and the Gmail accounts explicitly authorized for the task.
4. Any constraints: page count, location/commute framing, salary-sensitive positioning, or résumé format.

Use the existing project profile and previous résumé only as a **baseline**, not as proof of recency.

## Evidence Refresh Workflow

### 1. Load the Current Baseline

- Locate the newest available résumé/CV and the project master profile.
- Extract current employers, dates, roles, education, credentials, advisory service, recognitions, skills, and named partner organizations.
- Flag all claims that need reconfirmation or updating; do not blindly preserve dated claims.

### 2. Search for Role-Relevant Updates

Search narrowly and iteratively. Begin with the target role’s required competencies, then query authorized sources for evidence in these categories:

| Update category | Typical Gmail terms |
|---|---|
| New credentials / certificates | `certificate`, `completion`, `training`, `CTLE`, organization or program name |
| Advisory / board / committee service | `advisory`, `committee`, `board`, `TAC`, `mentor`, `panel` |
| Leadership / promotions / appointments | `appointed`, `selected`, `invitation`, `welcome`, `role`, `director` |
| Program delivery / facilitation | `residency`, `workshop`, `facilitator`, `curriculum`, `professional learning` |
| Partnerships / awards / public recognition | `award`, `proclamation`, `honor`, `grant`, `partner` |
| Digital / communications capabilities | `Mailchimp`, `Canva`, `WordPress`, `CRM`, `newsletter`, `campaign`, `survey` |

For this user, prioritize evidence from: Carnegie Hall/Weill Music Institute, NYC Arts in Education Roundtable, Community-Word Project, ArtsWestchester, Arts Connection, Rehabilitation Through The Arts, Building Beats, Playlab, Array Education, Relay Graduate School of Education, and named prospective employers.

When a Gmail connector has multiple accounts, inspect the connector configuration first and obtain approval to switch the active account if needed. Use `gmail_search_messages` to find records and `gmail_read_threads` to inspect decisive sources and attachments. Search each authorized inbox separately where appropriate.

### 3. Verify Before Inclusion

Classify each proposed update before adding it:

| Evidence level | Standard | Résumé treatment |
|---|---|---|
| **Verified** | Direct certificate, appointment notice, official email, signed letter, official program record, or user-confirmed fact | Include precisely, with dates and scope supported by the source. |
| **Supported** | Credible activity record shows participation but not a formal title or outcome | Use careful language such as “contributed to,” “participated in,” “served on a selection panel,” or “supported.” |
| **Unverified** | Inferred from a mailing list, self-description, ambiguous reference, or unsupported memory | Omit, or ask the user for confirmation when the claim is material. |

Never elevate an invitation into an appointment, a course enrollment into completion, a mailing-list recipient into a committee member, or collaboration into a formal board role.

Use the following verified examples only when the same records remain accessible in the current task:

- **Carnegie Hall Weill Music Institute, Music Educators Workshop:** certificate confirms Cornell Carelock completed **36 hours** from **September 2025 to June 2026**.
- **Carnegie Hall M.E.W. Teacher Advisory Committee (MEWTAC25):** committee channel/meeting notice identifies the recipient as part of the MEWTAC team in 2025.
- **Community-Word Project:** emails document Cornell’s teaching-artist work and participation in later-stage selection and evaluation for the Program Manager, Teaching Artist Sustainability & Arts Access role. Describe this as a **selection-panel contribution** unless a formal committee appointment source is found.

### 4. Build a Claim Ledger

Before drafting, create a compact private ledger in the working folder named `evidence-ledger.md` (do not deliver unless asked).

Use this table:

| Résumé claim | Evidence classification | Source / date | Exact safe wording |
|---|---|---|---|
| Carnegie Hall M.E.W. completion | Verified | Certificate email from Jordan Boucicaut, June 2026 | “Music Educators Workshop — Certificate of Completion (36 hours), Sep. 2025–Jun. 2026” |

The ledger ensures every material claim can be defended in a recruiter conversation.

### 5. Tailor to the Job, Not Just the Biography

Map verified evidence to the position’s requirements. For arts-education advocacy and community-engagement roles, foreground:

- Arts education ecosystem knowledge and youth-facing practice.
- Equity, access, cultural responsiveness, and social justice.
- Coalition relationships, advisory work, stakeholder engagement, and convening support.
- Advocacy communications: storytelling, writing, outreach, workshops, and public-facing materials.
- Program coordination, mentoring, facilitator experience, surveys/data where supported, and digital communications tools.

For every position, use the employer’s vocabulary where accurate, but never keyword-stuff or claim unsupported policy, legislative, CRM, fundraising, or data-analysis experience.

## Résumé Construction Rules

1. Use Cornell’s legal/professional name as **Cornell “Lord Judah” Carelock** unless an application requires a different legal-name treatment.
2. Use `judahblessent@gmail.com` and `914-661-3717` unless the user supplies replacements.
3. Keep targeted résumés to the posting’s requested page count; otherwise default to two pages.
4. Use a straightforward, ATS-readable layout with standard headings and no tables, charts, headshots, text boxes, or decorative graphics in the PDF.
5. Lead with a role-aligned professional summary and a compact capability section.
6. Prioritize recent, role-relevant, verified evidence over exhaustive chronology.
7. Write achievement bullets with action, context, and outcome—but do not invent metrics. Use only figures that can be sourced or user-confirmed.
8. State location honestly. Do not claim relocation, residency, or availability commitments that the user has not confirmed.
9. Include a source Markdown/Typst document when the user or application agent may need to revise details.

## Document Production & QA

1. For professional PDFs, read `typst-pdf-maker` and follow its routing, compile, verification, and visual-review requirements.
2. For a role requiring a one-file application packet, combine résumé and cover letter only after the user explicitly requests the combined packet; otherwise provide the résumé separately.
3. Verify the PDF is nonempty, parses correctly, has readable extracted text, stays within the page limit, and has no visual clipping or reflow issues.
4. Preserve the claim ledger, source file, evidence artifacts, build plan, and PDF verification report in the working folder.
5. Deliver the final PDF and source file. State only the key verified updates in the chat response.

## Recommended Final Handoff

Deliver:

- `[Cornell_Carelock_[Role]_Resume.pdf]` — application-ready, ATS-readable PDF.
- `[Cornell_Carelock_[Role]_Resume.typ]` or `.md` — editable source.

Summarize:

- Target role and date refreshed.
- Sources checked (at a high level, without exposing private email content).
- New verified additions included.
- Any material gap or claim intentionally excluded because evidence was not conclusive.

## Safety and Accuracy Boundaries

- Search only user-authorized accounts, project files, and services.
- Never share private email bodies, certificate identifiers, mailing-list membership, or personal addresses in the public résumé unless explicitly required and approved.
- Do not send applications or messages as part of résumé refresh alone.
- When a record conflicts with the existing résumé, favor the authoritative primary source and flag the conflict for the user if it affects a material claim.
- Use cautious wording when evidence proves contribution but not a formal title.
