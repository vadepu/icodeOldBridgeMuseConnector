# iCode Old Bridge Connector

Public API powering the iCode Old Bridge connector for Meta's Muse directory.

- `GET /campus` — campus info, hours, contact
- `GET /programs` — program catalog (`?age=`, `?track=`)
- `GET /schedule` — weekly schedule
- `GET /faq` — frequently asked questions
- `POST /waitlist` — join the Founding Families waitlist
- `GET /waitlist/count` — current waitlist size
- `GET /privacy`, `GET /terms` — policy pages
- `GET /health`, `GET /openapi.json` — ops

## Knowledge base

All campus content lives in `data.json` — edit it (no code changes), commit,
push, and Render redeploys automatically.

## Run locally

```bash
python -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/uvicorn app:app --port 8000
```

## Deploy

See `DEPLOY.md` (Render, free tier).
