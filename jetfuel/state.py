from typing import Dict, Union, List
from threading import Thread, Lock
from .cache import Cache
import requests
import time


_url: str = ""
_token: str = ""
_resolution: float = 5.0  # seconds
_caches: Dict[str, Cache] = {}
_commit_lock = Lock()


def init(url: str, token: str = "default", resolution: float = 5.0) -> None:
    """
    Initialize Jetfuel.

    Args:
        url: URL of jetfuel-server
        token: Login token
        resolution: Data collection resolution
    """
    global _url, _token, _resolution

    _url = url
    _token = token
    _resolution = resolution

    # Start data sending thread
    t = Thread(target=_commit)
    t.start()


def update(profiler_name: str, elapsed_time: float) -> None:
    """
    Receive update for a given profiler.

    Args:
        profiler_name: Which profiler
        elapsed_time: Time elapsed for task
    """
    global _caches, _url, _token, _commit_lock

    if profiler_name not in _caches:
        with _commit_lock:
            _caches[profiler_name] = Cache(profiler_name)

    _caches[profiler_name].update(elapsed_time)


def _commit() -> None:
    """
    Commit data to backend.
    """
    global _resolution

    while True:
        time.sleep(_resolution)

        with _commit_lock:
            periods: List[Dict[str, Union[str, Dict[str, Union[int, float]]]]] = []
            profiler_names = list(_caches.keys())

            try:
                # Acquire locks and calculate stats body
                for profiler_name in profiler_names:
                    cache = _caches[profiler_name]

                    # Ensure that cache updates, stat_calculation, and flushes are thread-safe
                    cache.lock.acquire()

                    # Calculate stats and add to request body
                    stats = cache.stats()
                    if stats is not None:
                        period_min, period_max, period_mean, period_count = stats
                        periods.append({
                            "name": profiler_name,
                            "stats": {
                                "min": period_min,
                                "max": period_max,
                                "mean": period_mean,
                                "count": period_count,
                            }
                        })

                # Commit to backend
                if len(periods) > 0:
                    requests.post(
                        f"{_url}/v1/commit",
                        json={
                            "timestamp": time.time(),
                            "periods": periods,
                        },
                        headers={
                            "Authorization": f"Bearer {_token}"
                        }
                    )

                # Flush cache data
                for cache in _caches.values():
                    cache.flush()
            except:
                pass
            finally:
                # Release locks
                for profiler_name in profiler_names:
                    cache = _caches[profiler_name]
                    cache.lock.release()
