from fastapi import FastAPI
from pydantic import BaseModel
from commons import database
from commons.logging import exception_handler


app = FastAPI()


class EventBody(BaseModel):
    timestamp: float
    name: str
    seconds: float


@app.post("/")
@exception_handler()
def post_event(event: EventBody) -> None:
    """
    Receive profiler event from client.

    Args:
        event: Event body containing name and seconds elapsed.
    """
    database.insert_event(
        event.timestamp,
        event.name,
        event.seconds,
    )

    return "OK"
