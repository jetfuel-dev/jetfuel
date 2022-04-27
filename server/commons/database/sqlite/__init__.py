import os
import time
from typing import Any, List, Optional, Tuple

import config
import sqlite3
from commons.logging import logger


def _upgrade_schema(version: int) -> None:
    """
    Upgrade schema by one version.

    Args:
        version: Next version

    Raises:
        FileNotFoundError: If schema with version number is not found
    """
    target_schema = os.path.join(os.path.dirname(__file__), f"{version}.sql")

    if not os.path.exists(target_schema):
        raise FileNotFoundError(f"\tSchema does not exist: {target_schema}")

    with open(target_schema, "r") as patch:
        logger.info(f"\tUpgrading schema to version: {version}")

        execute_script(patch.read())

        execute(
            """
                INSERT INTO schema_version (version, date)
                VALUES (?, ?);
            """,
            (version, int(time.time())),
        )


path = os.path.join(config.PROJECT_ROOT, "data")
if not os.path.exists(path):
    os.makedirs(path)

def _open_connection() -> sqlite3.Connection:
    return sqlite3.connect(os.path.join(path, "jetfuel.db"))


def execute_script(statement: str) -> None:
    conn = _open_connection()

    cursor = conn.cursor()
    cursor.executescript(statement)
    cursor.close()

    conn.commit()
    conn.close()


def execute(statement: str, args: Optional[Tuple[Any, ...]] = None) -> None:
    conn = _open_connection()

    cursor = conn.cursor()
    cursor.execute(statement, args)
    cursor.close()

    conn.commit()
    conn.close()


def retrieve_one(statement: str, args: Optional[Tuple[Any, ...]] = None) -> Tuple[Any]:
    conn = _open_connection()

    cursor = conn.cursor()
    result = cursor.execute(statement, args).fetchone()
    cursor.close()

    conn.commit()
    conn.close()

    return result


def retrieve_all(statement: str, args: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any]]:
    conn = _open_connection()

    cursor = conn.cursor()
    result = cursor.execute(statement, args).fetchall()
    cursor.close()

    conn.commit()
    conn.close()

    return result


def init() -> None:
    """
    Upgrades SQL Schema using incremental scripts. New setups will start
    with schema version 0, and incrementally build required schema.

    Raises:
        RuntimeError: If detected schema is higher than required.
    """
    logger.info("Initializing SQL")

    version = -1
    try:
        (version,) = retrieve_one("SELECT MAX(version) FROM schema_version;")
    except:  # No schema detected
        pass

    while version < config.SQL_VERSION:
        version += 1
        _upgrade_schema(version)
