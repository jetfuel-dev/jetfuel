from typing import List, Tuple, Optional
from threading import Lock


class Cache:
    def __init__(self, name: str) -> None:
        """
        Initialize thread-safe cache for a given profiler type.

        Args:
            name: Profiler name
            url: URL of Jetfuel-Server
            token: Auth token to use
        """
        self.name = name
        self.data: List[float] = []
        self.last_commit: float = 0
        self.lock = Lock()
    
    def stats(self) -> Optional[Tuple[float, float, float, int]]:
        """
        Calculate stats from data.

        Returns:
            period_min
            period_max
            period_mean
            period_count
        """
        if len(self.data) == 0:
            return

        # Calculate stats
        period_min = min(self.data)
        period_max = max(self.data)
        period_count = len(self.data)
        period_mean = sum(self.data) / period_count

        return period_min, period_max, period_mean, period_count

    def flush(self) -> None:
        """
        Flush data in cache.
        """
        # Flush data
        self.data = []


    def update(self, elapsed_time: float) -> None:
        """
        Update data.

        Args:
            elapsed_time: Time elapsed for a given Profiler.
        """
        with self.lock:
            self.data.append(elapsed_time)
