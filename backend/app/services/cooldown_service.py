import redis
import time
from app.config import settings

# Connect to Redis
redis_client = redis.from_url(settings.REDIS_URL)

COOLDOWN_SECONDS = 30

def check_cooldown(user_id: int):
    key = f"drop_cd:{user_id}"

    if redis_client.exists(key):
        return False

    redis_client.setex(key, COOLDOWN_SECONDS, "1")
    return True
