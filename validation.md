# Phase 2 — The Therapist: Validation

## How to know this phase succeeded

### 1. Server starts cleanly

```bash
uvicorn src.main:app --reload
```

No import errors, no crashes. Server is listening on `http://127.0.0.1:8000`.

### 2. Health check passes

```bash
curl http://127.0.0.1:8000/health
```

Expected: `{"status": "ok"}` with HTTP 200.

### 3. Session endpoint returns a therapist response

```bash
curl -X POST http://127.0.0.1:8000/session
```

Expected: HTTP 200 with JSON containing `session_id` (UUID string), `complaint` (non-empty string), and `therapist_response` (non-empty string from Claude).

### 4. Pytest suite passes

```bash
pytest tests/ -v
```

All tests green:
- `test_health.py` — `GET /health` returns 200 and `{"status": "ok"}`.
- `test_session.py` — `POST /session` returns 200 with valid `SessionResponse` shape and non-empty fields.

### 5. Merge criteria

All of the above pass. No unrelated files modified. Branch is rebased on `master` with no conflicts.
