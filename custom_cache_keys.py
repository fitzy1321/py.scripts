"""Create a memoized cache with custom keys"""

from datetime import timedelta
from random import randint
from cachetools import cached, TTLCache
from cachetools.keys import hashkey


# lambda arg names MUST match func arg names
@cached(
    cache=TTLCache(maxsize=10, ttl=timedelta(hours=24).total_seconds()),
    key=lambda obj_1, upper: hashkey(upper),
)
def some_func(obj_1, upper) -> int:
    return randint(0, upper)
