---
name: lord-judah-bmi-registration
description: "Reusable BMI work-registration workflow for Lord Judah songs, short-form video pieces, and related projects. Use for: preparing BMI registration intake, registering new works in BMI Online Services, applying Lord Judah default writer/publisher settings, handling browser-based submission safely, and accelerating repeat registrations once title and duration are known."
---

# Lord Judah BMI Registration

Use this skill when Lord Judah wants a work registered with BMI as early as possible in the production cycle, especially when the **title** and **duration** are already known and the rest of the registration can follow standard defaults.

## What this skill is for

This skill packages the observed BMI registration workflow for Lord Judah so future registrations can be handled quickly and consistently. It is designed for original works that usually follow the same publisher, writer, ownership, language, and work-type pattern.

Read `/home/ubuntu/skills/lord-judah-bmi-registration/references/intake-checklist.md` when you need the exact intake questions or default values. Read `/home/ubuntu/skills/lord-judah-bmi-registration/references/workflow-notes.md` when you need the observed step-by-step BMI screen logic.

## Standard operating assumption

Assume the registration is a **standard Lord Judah BMI registration** unless the user says otherwise. In a standard registration, proceed with these defaults:

| Field | Standard default |
|---|---|
| Language | English |
| Work type | All Other Genres |
| Work content | Music and Lyrics |
| Arrangement / translation | No |
| Samples or medleys | No |
| Artists listed in BMI | No |
| Recordings listed in BMI | No |
| Created for Film / TV / Theater / Music Library | No |
| Additional related information | Leave blank |

Also assume the standard publisher/writer setup from the saved BMI profile unless the user instructs otherwise.

## Minimum information required to begin

For a standard registration, do not block unnecessarily. You only need these two inputs to begin preparing the registration:

| Required input | Why it matters |
|---|---|
| Title | Needed for the work record |
| Duration | Needed for the BMI work info summary |

If the user provides only title and duration, proceed using the standard defaults. Only stop to ask questions if a non-standard condition appears.

## Non-standard conditions that require clarification

Pause and ask for clarification if any of the following apply:

| Condition | Why clarification is needed |
|---|---|
| Samples, medleys, or translation | Changes Step 2 selections |
| Co-writers or split publishers | Changes ownership/share fields |
| Artists or recordings should be listed | Changes Step 4 |
| Work created for film, TV, theater, or music library | Changes Step 4 |
| Alternate title or unusual metadata | May require extra entries |
| User wants special comments added | Additional related information can delay processing |

## Browser workflow

1. Open the BMI Online Services login or work-registration page.
2. If BMI requires login and the session is not already active, ask the user to take over the browser to log in.
3. Start a new work registration.
4. Enter the work information using the provided title and duration plus standard defaults.
5. In the **Other Works** step, use the standard original-work defaults unless the user gave contrary instructions.
6. In **Publishers & Writers**, use the saved Lord Judah publisher and writer profile entries unless the user specified other splits.
7. In **Artists & Recordings**, use standard defaults unless the user specifically wants entries there.
8. On the summary page, review all critical fields carefully.
9. Before clicking the final submission button, summarize the registration assumptions to the user and request confirmation.
10. Only after confirmation, submit the registration.
11. Save the confirmation details and report the successful submission back to the user.

## Critical safety rules

Always treat final BMI submission as a sensitive browser action. You must ask for explicit confirmation before clicking the final **Submit** button.

If login is required, open the BMI page first and then ask the user to take over the browser. Do not ask for browser takeover before the relevant page is open.

## Speed strategy

This skill exists to support parallel execution with content production. When Lord Judah says he has the **title** and **duration**, move the BMI registration forward immediately so that the registration process is already underway while the creative production continues.

If BMI presents a **Copy Work** option after submission, treat it as a future acceleration tool for similar registrations, but verify copied fields before submitting any new work.

## Recommended user-facing intake message

When the user wants a new registration, use a concise intake message patterned like this:

> Send me the title and duration. If this one is non-standard, also tell me whether it includes samples, co-writers, alternate titles, artists/recordings, or special split changes. Otherwise I will proceed with your standard BMI registration setup.

## Output expectations

After a successful registration, report these details back to the user when available:

| Output | Description |
|---|---|
| Registered title | The submitted work title |
| Duration | The submitted runtime |
| Registration status | Submitted / saved / pending confirmation |
| Any assumptions used | Defaults applied during registration |
| Any exceptions or follow-up needed | Items that may affect future royalties or metadata |

Keep the workflow lean. Do not over-question the user when the registration fits the standard Lord Judah template.
