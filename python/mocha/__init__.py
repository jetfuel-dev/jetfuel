from typing import Optional, Callable, Any
from functools import wraps
import requests
import time


_url: str = ""
_token: str = ""


def init(url: str, token: str = "default") -> None:
    """
    Initialize Mocha.

    Args:
        url: URL of mocha-server
        token: Login token
    """
    global _url, _token
    _url = url
    _token = token


def _event(name: str, seconds: float) -> None:
    """
    Fire a timing event to mocha-server.

    Args:
        name: Task name
        seconds: Seconds elapsed for task
    """
    requests.post(
        _url,
        json={
            "timestamp": time.time(),
            "name": name,
            "seconds": seconds,
        },
        headers={
            "Authorization": f"Bearer {_token}"
        }
    )


class Profiler:
    """
    Base Profiler that is used by all other convenience functions.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize Profiler.

        Args:
            name: Name of task being profiled.
        """
        self.name = name
    

    def start(self) -> None:
        """
        Start profiler.
        """
        self.start_time = time.perf_counter()


    def stop(self) -> None:
        """
        Stop profiler.
        """
        elapsed_time = time.perf_counter() - self.start_time
        _event(self.name, elapsed_time)


    def __enter__(self):
        """
        Start profiler as a context manager.
        """
        self.start()


    def __exit__(self, type, value, traceback):
        """
        Stop profiler context manager.
        """
        self.stop()


def start(name: str) -> Profiler:
    """
    Start a profiler.

    Args:
        name: Task name

    Returns:
        Profiler
    """
    profiler = Profiler(name=name)
    profiler.start()

    return profiler


def profiler(name: str) -> Callable[..., Callable[..., Any]]:
    """
    Profiler decorator.

    Args:
        name: Task name

    Returns:
        Function wrapper
    """
    def wrapper(f: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(f)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            with Profiler(name=name):
                return f(*args, **kwargs)
        return wrapped
    return wrapper
