# Phase 2 — The Therapist: Implementation Plan

## Task Group 1: Dependencies & Config

1. Add `fastapi`, `uvicorn`, `anthropic`, `pydantic`, `python-dotenv` to `requirements.txt`.
2. Create `.env.example` with `ANTHROPIC_API_KEY=your-key-here`.
3. Add `.env` to `.gitignore` (if not already present).

## Task Group 2: App Skeleton & Health Endpoint

4. Create `src/main.py` — FastAPI app instance, CORS middleware, and `GET /health` returning `{"status": "ok"}`.
5. Create `src/config.py` — load env vars via `python-dotenv`, expose `ANTHROPIC_API_KEY` and `CLAUDE_MODEL` (default `claude-sonnet-4-20250514`).

## Task Group 3: Pydantic Models

6. Create `src/models.py` with:
   - `SessionRequest` — empty body for now (complaint is hardcoded).
   - `SessionResponse` — fields: `session_id`, `complaint`, `therapist_response`.

## Task Group 4: Therapist Logic

7. Create `src/therapist.py`:
   - Hardcoded complaint string (a single comedic agent grievance).
   - Comedic system prompt establishing the therapist persona.
   - `async def diagnose(complaint: str) -> str` — calls Anthropic SDK, returns therapist response.

## Task Group 5: Session Endpoint

8. Add `POST /session` route in `src/main.py`:
   - Calls `diagnose()` with the hardcoded complaint.
   - Returns `SessionResponse` with a generated `session_id` (UUID).

## Task Group 6: Tests

9. Create `tests/test_health.py` — assert `GET /health` returns 200 and expected JSON.
10. Create `tests/test_session.py` — assert `POST /session` returns 200, valid `SessionResponse` shape, and non-empty `therapist_response`.
11. Create `tests/conftest.py` — shared `httpx.AsyncClient` fixture for FastAPI test client.
