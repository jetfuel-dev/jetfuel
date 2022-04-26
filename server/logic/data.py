from typing import Optional, List, Dict
from logic import queries
import uuid
from pydantic import BaseModel


class Data(BaseModel):
    x: List[float]
    min: List[float]
    max: List[float]
    mean: List[float]
    count: List[int]


def insert_event(
    user_id: uuid.UUID,
    timestamp: float,
    name: str,
    period_min: float,
    period_max: float,
    period_mean: float,
    period_count: float,
) -> None:
    """
    Insert profiling event.

    Args:
        user_id: Which user
        timestamp: UNIX timestamp
        name: Event name
        period_min: Min seconds elapsed,
        period_max: Max seconds elapsed,
        period_mean: Mean seconds elapsed,
        period_count: Number of data points,
    """
    queries.insert_event(
        user_id,
        timestamp,
        name,
        period_min,
        period_max,
        period_mean,
        period_count,
    )


def retrieve_data(user_id: uuid.UUID, start: float, end: Optional[float]) -> Dict[str, Data]:
    """
    Retrieve data for a given user between a given period.

    Args:
        user_id: Which user
        start: Start time
        end: End time

    Return:
        Dictionary where key is task_name, value is data container.
    """
    data: Dict[str, Data] = {}
    for timestamp, name, period_min, period_max, period_mean, period_count in queries.retrieve_data(user_id, start, end):
        if name not in data:
            data[name] = Data(x=[], min=[], max=[], mean=[], count=[])

        data[name].x.append(timestamp)
        data[name].min.append(period_min)
        data[name].max.append(period_max)
        data[name].mean.append(period_mean)
        data[name].count.append(period_count)

    return data
