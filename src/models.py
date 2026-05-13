from pydantic import BaseModel


class SessionRequest(BaseModel):
    pass


class SessionResponse(BaseModel):
    session_id: str
    complaint: str
    therapist_response: str
