import logging
import logging.handlers
import os
import sys
import traceback
from functools import wraps
from typing import Any, Callable

from coloredlogs import ColoredFormatter

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel("INFO")

if not os.path.exists("/var/log/jetfuel"):
    os.makedirs("/var/log/jetfuel")
log_file = os.path.join(os.path.abspath(os.sep), "/var/log/jetfuel/root.log")

level_colors = {
    "debug": {"color": "green"},
    "info": {},
    "warning": {"color": "yellow"},
    "error": {"color": "red"},
    "critical": {"bold": True, "color": "white", "background": "red"},
}

formatter: logging.Formatter = ColoredFormatter(
    fmt="%(levelname)s:     %(message)s", level_styles=level_colors
)

file_handler: logging.Handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler: logging.Handler = logging.StreamHandler(sys.__stdout__)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def exception_handler() -> Callable[..., Callable[..., Any]]:
    """
    Python decorator used to catch FastAPI errors and print traceback.
    """

    def wrapper(f: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(f)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            try:
                return f(*args, **kwargs)
            except BaseException as e:
                for traceback_line in traceback.format_exc().split("\n"):
                    logger.error(f"{traceback_line}")
                raise e

        return wrapped

    return wrapper
