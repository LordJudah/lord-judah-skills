# Volume II Individual Video Registry

**App location:** `/home/ubuntu/rap-report-recovered/client/src/data/volume2VideoHandoffs.json`

The registry starts empty. Add exactly one object per confirmed, released day after verification:

```json
[
  {
    "day": 1,
    "videoId": "AbCdEfG1234",
    "title": "Rap Profiles: Coke La Rock",
    "verifiedAt": "2026-10-08"
  }
]
```

Rules:

- `day` is an integer from 1 through 58 and must not be duplicated.
- `videoId` is the 11-character YouTube video ID. Never store a playlist ID or a full URL here.
- `title` is the public title returned by YouTube at verification time.
- `verifiedAt` is the verification date in `YYYY-MM-DD`.
- The record must match the artist and the day in `client/src/data/volume2Profiles.json`.
- A released report uses the direct link only when a matching valid record is present. All other reports continue to use the official Rap Profiles playlist fallback.
