# Phase 2 — The Therapist: Requirements

## Scope

This phase delivers the core therapy loop: a single API call sends a hardcoded agent complaint to Claude (acting as a comedic therapist) and returns the response.

### In Scope

- Anthropic SDK integration with configurable model.
- `POST /session` endpoint that generates a therapist response.
- `GET /health` endpoint (Phase 1 deliverable, built here since scaffold was empty).
- Pydantic request/response models.
- A single hardcoded complaint string (no agent profiles yet).
- Comedic therapist system prompt matching the satirical mission tone.

### Out of Scope

- Agent patient profiles and `GET /agents` (Phase 3).
- Structured diagnosis with severity ratings (Phase 4).
- Session persistence to disk (Phase 5).
- Multi-turn conversation (Phase 6).

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Complaint source | Single hardcoded string | Simplest to test deterministically; agent variety comes in Phase 3. |
| Therapist tone | Comedic from day one | Matches mission's satirical tone; more engaging for early demos. |
| Model default | `claude-sonnet-4-20250514` | Per tech-stack spec; configurable via env var. |
| Persistence | None | Session data is ephemeral this phase; persistence is Phase 5. |

## Context

- **Predecessor**: Phase 1 created the repo scaffold (`src/`, `tests/`, `specs/`, `.gitignore`, `requirements.txt`). No Python code exists yet.
- **Successor**: Phase 3 adds agent patient profiles that replace the hardcoded complaint.
- **Key dependency**: A valid `ANTHROPIC_API_KEY` is required at runtime. Tests that hit the real API need it too; tests without it should be clearly marked or skipped.
