"""
All queries that are made to external databases are defined here.
This allows us to add new database backends in the future in desired.
"""
import config
from typing import Optional, Tuple, List
from commons.database import sqlite
import uuid


if config.SQL_MODE == "sqlite":
    sqlite.init()


def create_user(email: str, user_id: uuid.UUID) -> None:
    """
    Create a user.

    Args:
        email: Unique user email
        user_id: Unique User ID
    """
    if config.SQL_MODE == "sqlite":
        sqlite.execute(
            """
                INSERT INTO users (user_id, email)
                VALUES (?, ?);
            """,
            (str(user_id), email)
        )


def get_user_id(email: str) -> Optional[uuid.UUID]:
    """
    Retrieve a user.

    Args:
        email: Unique user email
    """
    if config.SQL_MODE == "sqlite":
        try:
            (user_id_str,) = sqlite.retrieve_one(
                """
                    SELECT user_id
                    FROM users
                    WHERE email=?;
                """,
                (email,)
            )

            return uuid.UUID(user_id_str)
        except:
            return None


def update_api_token(user_id: uuid.UUID, api_token: str) -> None:
    """
    Update a user's api_token.

    Args:
        user_id: Which user
        api_token: User's api_token
    """
    if config.SQL_MODE == "sqlite":
        sqlite.execute(
            """
                UPDATE users SET api_token=? WHERE user_id=?;
            """,
            (api_token, str(user_id))
        )


def verify_api_token(api_token: str) -> Optional[uuid.UUID]:
    """
    Verify an api_token. Returns None if api_token is invalid.

    Returns:
        user_id
    """
    try:
        if config.SQL_MODE == "sqlite":
            (user_id,) = sqlite.retrieve_one(
                """
                    SELECT user_id FROM users WHERE api_token=?;
                """,
                (api_token,)
            )

            return user_id
    except:
        return None
    


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
    if config.SQL_MODE == "sqlite":
        sqlite.execute(
            """
                INSERT INTO events (user_id, timestamp, name, period_min, period_max, period_mean, period_count)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """,
            (user_id, timestamp, name, period_min, period_max, period_mean, period_count)
        )


def retrieve_data(
    user_id: uuid.UUID, start: float, end: Optional[float]
) -> List[Tuple[float, str, float, float, float, int]]:
    """
    Retrieve data for a given user between a given period.

    Args:
        user_id: Which user
        start: Start time
        end: End time

    Return:
        List:
            timestamp
            name
            period_min
            period_max
            period_mean
            period_count
    """
    if config.SQL_MODE == "sqlite":
        result: List[Tuple[float, str, float, float, float, int]] = []

        if end is None:
            result = sqlite.retrieve_all(
                """
                    SELECT timestamp, name, period_min, period_max, period_mean, period_count
                    FROM events
                    WHERE user_id=? AND timestamp>=?;
                """,
                (str(user_id), start)
            )
        else:
            result = sqlite.retrieve_all(
                """
                    SELECT timestamp, name, period_min, period_max, period_mean, period_count
                    FROM events
                    WHERE user_id=? AND timestamp>=? AND timestamp<=?;
                """,
                (str(user_id), start, end)
            )


        return result
