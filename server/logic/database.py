"""
All queries that are made to external databases are defined here.
This allows us to add new database backends in the future in desired.
"""
import config
from typing import Optional
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
