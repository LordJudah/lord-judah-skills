---
name: lord-judah-job-application
description: Automates the process of retrieving job opportunity emails, generating tailored Resumes and CVs for Cornell "Lord Judah" Carelock, converting them to PDFs, and emailing the application to the sender. Use when the user asks to apply for a job or program role based on an email.
---

# Lord Judah Job Application Workflow

This skill automates the end-to-end process of applying for jobs, grants, or program roles on behalf of Cornell "Lord Judah" Carelock. It ensures that his professional narrative—centering on youth empowerment, trauma-informed education, hip-hop culture, and community leadership—is consistently and accurately represented.

## Workflow Steps

When triggered to apply for a role based on an email, follow these exact steps:

### 1. Retrieve and Analyze the Email
- Use the `gmail` MCP server tools (`gmail_search_messages` and `gmail_read_threads`) to find and read the target email.
- Extract key information: Organization name, sender name and email, role title, core responsibilities, and required qualifications.

### 2. Draft Tailored Resume and CV
- Create two separate Markdown files: one for a concise Resume (1-2 pages) and one for a comprehensive Curriculum Vitae (CV).
- **Core Details to Include:**
  - **Name:** Cornell "Lord Judah" Carelock
  - **Contact:** judahblessent@gmail.com | 914-661-3717 | Hudson Valley, NY
  - **Current Roles:** CEO & Creative Director at Judah Bless Ent (Est. 2005); Director & Lead Teaching Artist at True He(ART) Academy (Est. 2016).
  - **Education:** Certificate in Creative Placemaking from New England College.
- **Tailoring Strategy:** Map Lord Judah's extensive experience in trauma-informed education, culturally responsive programming, and creative arts directly to the specific requirements of the role. Emphasize his ability to create safe, empowering environments for marginalized youth.

### 3. Format as PDFs
- Use the `manus-md-to-pdf` CLI tool to convert both the Resume and CV Markdown files into professional PDF documents.
- Ensure the output files are named clearly (e.g., `Lord_Judah_Resume.pdf` and `Lord_Judah_CV.pdf`).

### 4. Compose and Send the Application Email
- Draft a professional, mission-aligned cover letter/email addressed to the original sender.
- The tone should be warm, community-rooted, and reflective of Lord Judah's values (educational access, social justice, healing through art).
- Use the `gmail_send_messages` MCP tool to send the email, attaching both the Resume and CV PDFs.

## Key Themes & Vocabulary to Utilize
- **Youth Empowerment & Mentorship**
- **Trauma-Informed & Culturally Responsive Education**
- **Social-Emotional Learning (SEL)**
- **Creative Expression (Hip-Hop, Digital Arts, Storytelling)**
- **Community Building & Immigrant Justice**
- **Immersive / Residential Program Support**

## Required Tools
- `gmail` MCP server (`gmail_search_messages`, `gmail_read_threads`, `gmail_send_messages`)
- `file` tool (for drafting Markdown)
- `shell` tool with `manus-md-to-pdf` (for PDF conversion)
