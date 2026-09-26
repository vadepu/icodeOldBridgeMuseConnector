# Deploy the connector API (5 minutes, free)

The API is built and tested. It needs a stable public URL for Meta's review
and for your Muse to call it. Easiest path: Render's free tier.

## Steps

1. Push this folder to a GitHub repo (e.g. `icode-old-bridge-connector`).
   From a terminal where you have git:
   `git init && git add -A && git commit -m "iCode Old Bridge connector"`,
   then create the repo on github.com and `git push`.
2. Go to render.com → sign up/log in → **New +** → **Web Service** →
   **Build and deploy from a Git repository** → connect the repo.
3. Render auto-detects `render.yaml`. Keep the free plan. Click **Deploy**.
4. When it goes live you get a URL like
   `https://icode-old-bridge-connector.onrender.com`.
5. Open `https://<your-url>/health` — you should see `{"ok": true, ...}`.

## After deploy

- Update the Base URL in `~/workspace/skills/icode-old-bridge/SKILL.md`
  so your Muse calls the live service.
- Free-tier note: Render sleeps after inactivity; first call can take ~30s
  to wake. For Meta's review this is fine, but if you want instant responses
  later, the $7/mo starter plan keeps it always on.

## Updating info later (your KB)

All campus info, programs, and FAQs live in `data.json` — plain text, no code.
To update: edit `data.json` (or just tell Muse what to change), commit, and
push. Render redeploys automatically and every Muse user gets the new answers
instantly.
- Then tell Muse: "Use my iCode Old Bridge connector skill" and try:
  "What coding classes are there for my 9-year-old near Old Bridge?"
