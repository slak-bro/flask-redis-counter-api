from os import getenv

import redis

REDIS_HOST = getenv("REDIS_HOST", default="localhost")
REDIS_PORT = getenv("REDIS_PORT", default=6379)
REDIS_DB = getenv("REDIS_DB", default=0)
REDIS_KEY_PREFIX = getenv("REDIS_KEY_PREFIX", default=None)

APPLICATION_PREFIX = "counter_api"
REDIS_PREFIX = (
    f"{REDIS_KEY_PREFIX}:{APPLICATION_PREFIX}"
    if REDIS_KEY_PREFIX is not None
    else APPLICATION_PREFIX
)
COUNTER_KEY = f"{REDIS_PREFIX}:counter"

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def increment():
    r.incr(COUNTER_KEY)


def get_value():
    v = r.get(COUNTER_KEY)
    if v is None:
        val = 0
    else:
        val = int(v)
    return {"value": val}
