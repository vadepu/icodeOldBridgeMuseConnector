"""iCode Old Bridge — Muse Connector API.

Public web service that powers the iCode Old Bridge connector for Meta Muse.
Any agent (or the Meta directory review team) can call these endpoints to
answer questions about the campus and to join the Founding Families waitlist.

Run: ./venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000
Docs: /docs  OpenAPI: /openapi.json
"""
import sqlite3
import uuid
import json
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "waitlist.db"

# ---------------------------------------------------------------------------
# Knowledge base — edit data.json to update campus info, programs, FAQs.
# No code changes needed. Redeploy (or restart) to pick up edits.
# ---------------------------------------------------------------------------
def load_kb() -> dict:
    with open(BASE_DIR / "data.json", encoding="utf-8") as f:
        return json.load(f)


KB = load_kb()
CAMPUS = KB["campus"]
PROGRAMS = KB["programs"]
FAQ = KB["faq"]
PRIVACY_TEXT = KB["privacy"]
TERMS_TEXT = KB["terms"]


class WaitlistSignup(BaseModel):
    parent_name: str = Field(..., min_length=1, max_length=120)
    contact: str = Field(
        ..., min_length=3, max_length=160, description="Phone number or email"
    )
    contact_type: str = Field("phone", pattern="^(phone|email)$")
    child_age: int = Field(..., ge=3, le=18)
    child_name: str = Field("", max_length=120)
    interests: list[str] = Field(default_factory=list, max_length=10)
    notes: str = Field("", max_length=500)


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """CREATE TABLE IF NOT EXISTS waitlist (
            id TEXT PRIMARY KEY,
            parent_name TEXT NOT NULL,
            contact TEXT NOT NULL,
            contact_type TEXT NOT NULL,
            child_age INTEGER NOT NULL,
            child_name TEXT DEFAULT '',
            interests TEXT DEFAULT '[]',
            notes TEXT DEFAULT '',
            created_at TEXT NOT NULL
        )"""
    )
    return conn


app = FastAPI(
    title="iCode Old Bridge Connector",
    description=(
        "Public API for the iCode Old Bridge Muse connector: campus info, "
        "programs by age, FAQs, and Founding Families waitlist signup."
    ),
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


@app.get("/", tags=["meta"])
def root():
    return {
        "service": "iCode Old Bridge Connector",
        "version": "1.0.0",
        "campus_status": CAMPUS["status"],
        "endpoints": [
            "/campus", "/programs", "/programs?age={n}", "/schedule",
            "/faq", "/waitlist (POST)", "/waitlist/count", "/privacy",
        ],
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@app.get("/campus", tags=["info"])
def campus():
    return CAMPUS


@app.get("/programs", tags=["info"])
def programs(age: int | None = None, track: str | None = None):
    """List programs; optionally filter by child age or track."""
    result = PROGRAMS
    if age is not None:
        result = [p for p in result if p["min_age"] <= age <= p["max_age"]]
    if track is not None:
        result = [p for p in result if p["track"] == track.lower()]
    return {"count": len(result), "programs": result}


@app.get("/schedule", tags=["info"])
def schedule():
    return {
        "status": CAMPUS["status"],
        "detail": CAMPUS["status_detail"],
        "waitlist": "open",
        "milestones": [
            {"phase": "Founding Families waitlist", "state": "open_now"},
            {"phase": "Trial classes", "state": "announced_to_waitlist_first"},
            {"phase": "Campus opens", "state": "fall_2026"},
        ],
    }


@app.get("/faq", tags=["info"])
def faq():
    return {"count": len(FAQ), "faqs": FAQ}


@app.post("/waitlist", tags=["waitlist"], status_code=201)
def join_waitlist(signup: WaitlistSignup):
    """Join the Founding Families waitlist. Free; no payment info collected."""
    import json

    entry_id = uuid.uuid4().hex[:10]
    created = datetime.now(timezone.utc).isoformat()
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO waitlist VALUES (?,?,?,?,?,?,?,?,?)",
            (
                entry_id,
                signup.parent_name.strip(),
                signup.contact.strip(),
                signup.contact_type,
                signup.child_age,
                signup.child_name.strip(),
                json.dumps(signup.interests),
                signup.notes.strip(),
                created,
            ),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Duplicate signup id, retry.")
    finally:
        conn.close()
    return {
        "confirmation_id": entry_id,
        "message": (
            f"Welcome to the Founding Families waitlist, {signup.parent_name.strip()}! "
            "iCode Old Bridge opens Fall 2026 — we'll reach out at "
            f"{signup.contact.strip()} with priority enrollment and early rates."
        ),
        "created_at": created,
    }


@app.get("/waitlist/count", tags=["waitlist"])
def waitlist_count():
    conn = get_db()
    n = conn.execute("SELECT COUNT(*) FROM waitlist").fetchone()[0]
    conn.close()
    return {"founding_families": n, "waitlist": "open"}


@app.get("/privacy", tags=["meta"], response_class=PlainTextResponse)
def privacy():
    return PRIVACY_TEXT


@app.get("/terms", tags=["meta"], response_class=PlainTextResponse)
def terms():
    return TERMS_TEXT


@app.get("/health", tags=["meta"])
def health():
    return {"ok": True, "time": datetime.now(timezone.utc).isoformat()}
