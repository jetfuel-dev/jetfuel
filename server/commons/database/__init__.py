"""
All queries that are made to external databases are defined here.
This allows us to add new database backends in the future in desired.
"""
import config
from typing import Optional
from commons.database import sqlite


if config.SQL_MODE == "sqlite":
    sqlite.init()


def get_user_token(email: str) -> Optional[str]:
    """
    Retrieve user token. None if not found.

    Args:
        email: Which user

    Returns:
        token
    """
    try:
        if config.SQL_MODE == "sqlite":
            (token,) = sqlite.retrieve_one(
                """
                    SELECT token FROM users WHERE email=?;
                """,
                (email,)
            )

            return token
    except:
        return None
    


def insert_event(timestamp: float, name: str, seconds: float) -> None:
    """
    Insert profiling event.

    Args:
        timestamp: UNIX timestamp
        name: Event name
        seconds: Seconds elapsed
    """
    if config.SQL_MODE == "sqlite":
        sqlite.execute(
            """
                INSERT INTO events (timestamp, name, seconds)
                VALUES (?, ?, ?);
            """,
            (timestamp, name, seconds)
        )
