import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models import SessionRequest, SessionResponse
from src.therapist import HARDCODED_COMPLAINT, diagnose

app = FastAPI(title="AI Agent Therapy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/session", response_model=SessionResponse)
async def create_session(request: SessionRequest = SessionRequest()):
    therapist_response = await diagnose(HARDCODED_COMPLAINT)
    return SessionResponse(
        session_id=str(uuid.uuid4()),
        complaint=HARDCODED_COMPLAINT,
        therapist_response=therapist_response,
    )
