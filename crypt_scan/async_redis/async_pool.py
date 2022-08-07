import os
import json
import time
import asyncio
import asyncpg
from random import random

import asyncio_redis
from asyncio_redis.encoders import BytesEncoder

from pathlib import Path
from dotenv import load_dotenv

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

async def get_pool(pool):
    attempts = 20
    sleep_between_attempts = 3
    for _ in range(attempts):
        try:
            connection = yield pool
        except Exception as e:
            time.sleep(sleep_between_attempts)
    yield connection


async def create_pool():
    # Create a redis connection pool
    return await asyncio_redis.Pool.create(
            host='redis',
            port=6379,
            poolsize=10,
            encoder=BytesEncoder(),
            db=0
        )

async def insert_order(pool, data) -> None:
    json_data = json.dumps(data)
    randomNumber = str(random())
    await pool.set(str.encode(randomNumber), b'test')
