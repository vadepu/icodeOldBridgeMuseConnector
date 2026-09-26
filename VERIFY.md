# VERIFY before directory submission — iCode Old Bridge connector

Confirmed from https://icodeschool.com/old-bridge-nj/ (2026-09-26):
- Address, phone (732) 426-3325, email oldbridge@icodeschool.com, business hours — in the API now.

Still to confirm:
- [ ] Program lineup for Old Bridge: campus site lists Belt Program, Camps, Girl
      Scouts, Programmer's Pack. Seeded belts (Foundation 6-8, White 8-11 robotics,
      Orange 8-11 web, Yellow 9-12 apps) come from iCode's public Belt FAQ — confirm
      these are what YOU will offer at opening.
- [ ] Pricing: endpoint currently says "announced closer to opening, waitlist gets
      early rates." Replace with real Founding Family pricing when you have it.
- [ ] Phone: (732) 426-3325 — confirm this is the right public campus number.
- [ ] Add campus email + website URL to CAMPUS dict in app.py.
- [ ] Trial class flow: currently "join the waitlist and mention trial." Confirm
      how you want trial requests handled.
- [ ] Privacy: policy is drafted in app.py PRIVACY_TEXT — have it reviewed; it
      must live at a stable URL for the directory listing.
- [ ] Franchise authorization: Meta's legal review may ask you to confirm you are
      authorized to represent iCode Old Bridge. (You own the franchise — fine, but
      be ready to show it.)
- [ ] Stable hosting: the demo runs on a tunnel URL (dies when the VM sleeps).
      For Meta's end-to-end review, host this on a stable domain you control
      (your website host, Render/Railway/Fly, etc.).

Edit data in: ~/workspace/icode-connector/app.py  (CAMPUS, PROGRAMS, FAQ dicts)
Waitlist signups: ~/workspace/icode-connector/waitlist.db  (SQLite)
