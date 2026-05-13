import uuid
import pytest


@pytest.mark.asyncio
async def test_session_returns_valid_response(client):
    response = await client.post("/session")
    assert response.status_code == 200

    data = response.json()
    assert "session_id" in data
    uuid.UUID(data["session_id"])
    assert isinstance(data["complaint"], str) and len(data["complaint"]) > 0
    assert isinstance(data["therapist_response"], str) and len(data["therapist_response"]) > 0
