from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from pydantic import BaseModel
from commons import database
from commons.logging import exception_handler
from logic import auth
from typing import Optional


app = FastAPI()


# Bearer token for client events
security = HTTPBearer()


class EventBody(BaseModel):
    timestamp: float
    name: str
    seconds: float



@app.post("/")
@exception_handler()
def post_event(event: EventBody, credentials: HTTPBasicCredentials = Depends(security)) -> None:
    """
    Receive profiler event from client.

    Args:
        event: Event body containing name and seconds elapsed.
        credentials: Bearer with API Token
    """
    api_token = credentials.credentials
    if not auth.verify_api_token(api_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    database.insert_event(
        event.timestamp,
        event.name,
        event.seconds,
    )

    return "OK"
