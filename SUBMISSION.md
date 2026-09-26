# Connector submission form — FILLED (iCode Old Bridge)
Field-by-field answers for the Overview step at muse.ai/platform.
Facts from https://icodeschool.com/old-bridge-nj/.

## Connector name
iCode Old Bridge

## Company or developer
iCode Old Bridge
(If your franchise legal entity name differs, use that instead.)

## Product website
https://icodeschool.com/old-bridge-nj/

## Example prompts
- "What coding classes are available near Old Bridge for my 9-year-old?"
- "When does iCode Old Bridge open, and how do we join the waitlist?"
- "Do you offer robotics classes for kids? What are your hours?"
- "Sign my family up for the Founding Families waitlist."

## Connector icon
Upload `connector-icon-codie-512.png` (in this folder — 512×512 PNG, ready).

## Payments
Choose "No payments" / "Does not accept payments" (this connector takes no
payments; the waitlist is free).

## Your name
[YOUR FULL NAME — fill in]

## Work email
oldbridge@icodeschool.com

## Support email or URL
oldbridge@icodeschool.com

## Your privacy policy
{YOUR DEPLOYED URL}/privacy
(Deploy first per DEPLOY.md, then paste the full URL, e.g.
https://icode-old-bridge-connector.onrender.com/privacy)

## Your terms of service
{YOUR DEPLOYED URL}/terms
(e.g. https://icode-old-bridge-connector.onrender.com/terms)

## Anything else? (optional)
Pre-opening campus (opens Fall 2026). The connector's main action is the free
Founding Families waitlist; program data is marked planned and will be
finalized at opening. No test account needed — all endpoints are public:
GET /health, /campus, /programs?age={n}, /schedule, /faq, POST /waitlist,
GET /waitlist/count, /privacy, /terms, /openapi.json.

---
## Step 2 (Technical specs) — answers for the next screen
- Connector type: API (REST, not MCP)
- API base URL: your deployed URL (from DEPLOY.md)
- API docs: {base}/openapi.json and {base}/docs
- Authentication: none required
- Test: POST {base}/waitlist with
  {"parent_name":"Review Test","contact":"review@example.com",
   "contact_type":"email","child_age":10,"interests":["coding"]} → 201
  (test rows are purged; safe to submit)
