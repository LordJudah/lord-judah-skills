# ManyChat Flow Template — LJB Course Launch Workflow

Replace `{VARIABLES}` before use. Always use ManyChat for comment auto-replies — never Make.com.

---

## Trigger Setup

1. ManyChat Dashboard → **Automation → New Flow → Start from Scratch**
2. Click **Add Trigger**
3. Select **Instagram → User comments on your Post or Reel**
4. Set condition: **"Message contains specific words"**
5. Enter keyword: `{KEYWORD}` (and lowercase/mixed-case variants)
6. Save trigger

---

## Public Comment Reply (Rotate 3 Variants)

Add a "Reply to Comment" action. ManyChat rotates these automatically:

- "Cypher is open. 🔱 Just sent the link to your DMs!"
- "Got you. Check your requests for the direct link. 📩"
- "Link secured. Check your DMs. 👑"

---

## DM Step 1 — Initial DM (Immediate)

**Message:**
```
Peace. 🔱 The cypher is officially open.

{COURSE_TITLE} is built for those ready to master their craft and amplify their voice.
{MODULE_COUNT} modules. Video lessons. Creative exercises.

Tap below to secure your spot and start the first module today. 👇
```

**Button:**
- Title: `ENROLL NOW`
- Action: Open Website
- URL: `{PRODUCT_URL}`

---

## Action — Add Tag (Immediate)

Add tag: `Course Lead - {COURSE_TITLE}`

Optional: Add tag `Clicked - {COURSE_TITLE}` when user clicks the button (requires ManyChat Pro).

---

## Smart Delay — 24 Hours

Add a **Smart Delay** step set to **24 hours**.

*Note: Instagram's API requires interaction within the 24-hour window. This is the maximum safe delay for follow-up DMs.*

---

## DM Step 2 — Follow-Up DM (After 24 Hours)

**Message:**
```
Just checking in. Did the link come through okay?

If you're on the fence, remember the final project for this course is {FINAL_PROJECT}.
It's about finding your frequency.

Let me know if you have any questions about the modules or the process. I'm here. 👑
```

**Quick Replies (Optional):**
- "Got the link!"
- "I have a question"

---

## Testing

1. Click **Publish** in ManyChat
2. Click **Preview** → send to your own Instagram account
3. Verify the link opens the correct Shopify product page
4. Verify formatting looks clean on mobile

---

## Notes

- This flow works alongside existing STREAM and MERCH flows — all three are part of the unified ManyChat comment automation system
- Always verify the `{PRODUCT_URL}` is the live Shopify product URL before publishing
- Tag naming convention: `Course Lead - {COURSE_TITLE}` (for future retargeting segments)
