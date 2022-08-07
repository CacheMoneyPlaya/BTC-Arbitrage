import os
import time
import asyncio
import asyncpg
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)


# async def get_pool(dsn):
#     attempts = 20
#     sleep_between_attempts = 3
#     for _ in range(attempts):
#         try:
#             pool = asyncio.run(create_pool())
#         except Exception as e:
#             time.sleep(sleep_between_attempts)
#     return pool


async def create_pool():
    # Create a database connection pool
    return await asyncpg.create_pool(
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASS'),
        host=os.getenv('PG_HOST'),
        port=os.getenv('PG_PORT'),
        database=os.getenv('PG_DATABASE'),
        command_timeout=60,
        max_size=100
    )

async def insert_order(connection, order, exchange) -> None:
    await connection.execute(
        '''INSERT INTO {}_side(asset, exchange, price, size, order_value)
        VALUES($1, $2, $3, $4, $5)'''.format(str(order.get('side')).lower()),
        'BTC',
        order.get('exchange'),
        order.get('price'),
        order.get('quantity'),
        order.get('order_value')
    )
