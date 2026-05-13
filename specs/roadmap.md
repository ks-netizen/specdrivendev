# AgentClinic — Roadmap

Nano phases. Each phase is 1-3 features, completable in a day or less.

---

## Phase 1 — Hello Clinic

- Project setup: dependencies, .env config, FastAPI app skeleton
- Single `GET /health` endpoint to verify the server runs

## Phase 2 — The Therapist

- Integrate Anthropic SDK
- `POST /session` — send a hardcoded agent complaint, get a therapist response from Claude
- Pydantic models for request/response

## Phase 3 — The Patient

- Agent "patient" profiles: name, personality, common complaints
- `GET /agents` — list available agent patients
- `POST /session` now accepts an agent ID and generates a complaint in-character

## Phase 4 — The Diagnosis

- Therapist returns a structured response: diagnosis, advice, severity rating
- Humorous diagnosis categories (e.g., "Chronic Vagueness Syndrome", "Prompt Injection PTSD")

## Phase 5 — Session History

- Save sessions to JSON files
- `GET /sessions` — list past sessions
- `GET /sessions/{id}` — retrieve a specific session

## Phase 6 — Multi-Turn Therapy

- Support back-and-forth conversation within a session
- `POST /sessions/{id}/reply` — continue an existing session

## Phase 7 — The Waiting Room

- Multiple agents can be "in the clinic" at once
- `GET /waiting-room` — see which agents are waiting
- Random agent complaints and walk-in scenarios

## Phase 8 — Polish & Personality

- Richer agent backstories and complaint variety
- Therapist personality tuning (warm, sarcastic, clinical, etc.)
- Error handling and input validation hardening

## Phase 9+ — Future Ideas

- Simple web frontend
- Agent mood tracking over time
- "Group therapy" sessions with multiple agents
- Leaderboard: most traumatized agent
