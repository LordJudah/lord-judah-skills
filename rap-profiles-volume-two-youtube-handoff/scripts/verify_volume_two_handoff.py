#!/usr/bin/env python3
"""Verify that a pasted YouTube video URL is public and in the Rap Profiles playlist."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen

PLAYLIST_ID = "PLew51Xxv9eLA"
API_ROOT = "https://www.googleapis.com/youtube/v3"


def video_id_from_url(value: str) -> str | None:
    parsed = urlparse(value.strip())
    host = parsed.netloc.lower().removeprefix("www.")
    if host == "youtu.be":
        candidate = parsed.path.strip("/").split("/")[0]
    elif host in {"youtube.com", "m.youtube.com", "music.youtube.com"}:
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [""])[0]
        elif parsed.path.startswith("/shorts/") or parsed.path.startswith("/embed/"):
            candidate = parsed.path.strip("/").split("/")[1]
        else:
            candidate = ""
    else:
        candidate = ""
    return candidate if re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate) else None


def request_json(url: str) -> dict:
    with urlopen(url, timeout=20) as response:  # nosec B310: trusted YouTube API endpoint
        return json.load(response)


def playlist_contains(video_id: str, api_key: str) -> bool:
    page_token = None
    while True:
        url = f"{API_ROOT}/playlistItems?part=contentDetails&playlistId={PLAYLIST_ID}&maxResults=50&key={api_key}"
        if page_token:
            url += f"&pageToken={page_token}"
        data = request_json(url)
        if any(item.get("contentDetails", {}).get("videoId") == video_id for item in data.get("items", [])):
            return True
        page_token = data.get("nextPageToken")
        if not page_token:
            return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public YouTube watch, short, embed, or youtu.be URL")
    args = parser.parse_args()
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print(json.dumps({"accepted": False, "reason": "YOUTUBE_API_KEY is not available"}))
        return 2

    video_id = video_id_from_url(args.url)
    if not video_id:
        print(json.dumps({"accepted": False, "reason": "The URL does not contain a valid YouTube video ID"}))
        return 2

    data = request_json(f"{API_ROOT}/videos?part=snippet,status&id={video_id}&key={api_key}")
    items = data.get("items", [])
    if len(items) != 1:
        print(json.dumps({"accepted": False, "videoId": video_id, "reason": "The video was not found"}))
        return 2

    item = items[0]
    privacy = item.get("status", {}).get("privacyStatus")
    if privacy != "public":
        print(json.dumps({"accepted": False, "videoId": video_id, "privacyStatus": privacy, "reason": "The video is not public"}))
        return 2

    in_playlist = playlist_contains(video_id, api_key)
    result = {
        "accepted": in_playlist,
        "videoId": video_id,
        "title": item.get("snippet", {}).get("title", ""),
        "publishedAt": item.get("snippet", {}).get("publishedAt", ""),
        "playlistId": PLAYLIST_ID,
        "reason": "Verified public and present in the Rap Profiles playlist" if in_playlist else "Public video is not yet in the Rap Profiles playlist",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if in_playlist else 2


if __name__ == "__main__":
    sys.exit(main())
