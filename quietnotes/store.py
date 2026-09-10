"""Where notes live: one JSON file under the user's state directory."""
import json
import os
import time
from pathlib import Path


def state_path() -> Path:
    base = os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local" / "state"))
    return Path(base) / "quietnotes" / "notes.json"


def load() -> list[dict]:
    p = state_path()
    if not p.exists():
        return []
    return json.loads(p.read_text())


def save(notes: list[dict]) -> None:
    p = state_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(notes, indent=2))


def add(text: str) -> dict:
    notes = load()
    note = {"id": len(notes) + 1, "text": text.strip(), "at": int(time.time())}
    notes.append(note)
    save(notes)
    return note


def remove(note_id: int) -> bool:
    notes = load()
    kept = [n for n in notes if n["id"] != note_id]
    if len(kept) == len(notes):
        return False
    save(kept)
    return True
