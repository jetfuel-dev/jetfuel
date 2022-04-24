"""
All queries that are made to external databases are defined here.
This allows us to add new database backends in the future in desired.
"""
import config
from commons.database import sqlite

if config.SQL_MODE == "sqlite":
    sqlite.init()

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
