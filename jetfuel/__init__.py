"""
 Calculate stats (min, max, mean, count), then fire event to Jetfuel-Server
                                    ^
                                    |
           Event Cache (stores raw performance profiling events)
                                    ^
                                    |
                              Profiler Class
                                    ^
                                    |
        Syntactic Sugar (context manager, function decorator, etc.)
"""

from .state import init as init
from .profiler import Profiler as Profiler
from .profiler import profiler as profiler
from .profiler import start as start
from .demo import demo as demo
