# AgentClinic — Tech Stack

## Language

- **Python 3.11+**

## Framework

- **FastAPI** — REST API backend for serving therapy sessions
- **Uvicorn** — ASGI server to run FastAPI

## AI

- **Anthropic SDK** (`anthropic`) — Claude as the therapist and agent voice
- Claude model: `claude-sonnet-4-20250514` (default, configurable)

## Data

- **Pydantic** — request/response models and validation
- **JSON files** — lightweight persistence for early phases (no database yet)

## Testing

- **pytest** — unit and integration tests
- **httpx** — async test client for FastAPI

## Dev Tools

- **ruff** — linting and formatting
- **python-dotenv** — environment variable management (.env for API keys)

## Not Yet (Future Phases)

- Database (SQLite or PostgreSQL)
- Frontend (HTML/JS or React)
- Docker / deployment
