---
name: city-views-campaign-manager
description: Manages the curation, construction, posting, and archiving of City Views App promotional campaigns. Use this skill when tasked with creating social media posts, organizing campaign assets, or managing the City Views content library in Google Drive.
---

# City Views Campaign Manager

This skill provides the workflow and standards for managing City Views App promotional campaigns. It ensures that all content aligns with Lord Judah's brand identity, utilizes the established Google Drive asset library, and follows a structured posting and archiving process.

## Core Workflow

When tasked with creating or managing a City Views campaign, follow these steps:

### 1. Asset Retrieval & Matching
- **Access the Library:** Use the `gws` CLI or `rclone` to access the `CITY VIEWS/Campaign Asset Library` in Google Drive.
- **Locate Assets:** Find the relevant images (App Pages, Merch, Products, etc.) requested by the user.
- **Locate Scripts:** Find the corresponding campaign copy in `CITY VIEWS/Campaign Scripts & Copy`.
- **Match:** Ensure the visual asset perfectly aligns with the tone and message of the script.

### 2. Content Construction & Review
- **Review Brand Alignment:** Ensure the combined asset and script adhere to the Lord Judah Visual Identity and Typography guidelines (bold, intentional, intelligent, culturally authentic).
- **Format for Platform:** Adapt the script for the specific social media platform (e.g., shorter for Twitter/X, visually focused for Instagram, video-centric for TikTok).
- **Final Polish:** Check for advanced lyricism principles, storytelling elements, and clear calls to action (CTAs) directing users to the City Views App or Merch store.

### 3. Posting & Execution
- **Schedule or Post:** Use the appropriate social media integration tools (e.g., Instagram MCP) to publish the content.
- **Verify:** Confirm the post is live and formatted correctly.

### 4. Archiving & Logging (Crucial Step)
- **Move Assets:** Once posted, move the used image(s) and script from their active folders into the `CITY VIEWS/Posted Archive/[Current Month]` folder in Google Drive.
- **Update Log:** Append an entry to the `CITY VIEWS/Campaign Logs & Analytics/Campaign_Log.csv` (or create it if it doesn't exist). The log should include:
  - Date & Time
  - Platform
  - Asset Filename
  - Script Snippet
  - Post URL (if available)

## Brand & Tone Guidelines

- **Visuals:** High contrast, urban/cultural environments, futuristic overlays. Avoid generic stock imagery.
- **Typography:** Bold sans-serif for headlines, clean body text. Confident and direct tone.
- **Messaging:** Blend classic boom-bap authenticity with futuristic, AI-driven concepts. Focus on empowerment, community uplift, and edutainment.

## Google Drive Folder Structure Reference

The master library is located at `manus_google_drive:CITY VIEWS/`. Key subfolders include:
- `Campaign Asset Library/` (App Pages, Merch, Products, Branding)
- `Campaign Scripts & Copy/` (Platform-specific copy)
- `Active Campaigns/` (Currently running initiatives)
- `Scheduled Posts/` (Ready to go live)
- `Posted Archive/` (Completed campaigns, organized by month)
- `Campaign Logs & Analytics/` (Tracking sheets)

Always maintain this structure and keep active folders clean by diligently archiving posted content.
