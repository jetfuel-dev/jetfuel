from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from pydantic import BaseModel
from commons.logging import exception_handler, logger
from logic import auth, database
from typing import List
import config


app = FastAPI()


# Bearer token for client events
security = HTTPBearer()


class EventBody(BaseModel):
    # Represents a given period of data collection
    class TaskPeriod(BaseModel):
        class Stats(BaseModel):
            min: float
            max: float
            mean: float
            count: int

        name: str
        stats: Stats

    timestamp: float
    periods: List[TaskPeriod]



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
    user_id = auth.verify_api_token(api_token)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    for period in event.periods:
        database.insert_event(
            user_id,
            event.timestamp,
            period.name,
            period.stats.min,
            period.stats.max,
            period.stats.mean,
            period.stats.count,
        )

    return "OK"


@app.on_event("startup")
def startup() -> None:
    logger.info("")
    logger.info("Mocha Server")
    logger.info("------------")
    logger.info("")

    # Add Default User
    if config.DEFAULT_USER:
        try:
            user_id = auth.create_user(email="default")
            auth.generate_api_token(user_id=user_id, api_token="default")
        except:
            # Default user already exists
            pass

    logger.info("")
    logger.info("READY")
    logger.info("")
