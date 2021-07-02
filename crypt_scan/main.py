import os
import asyncio
from dotenv import load_dotenv
from async_database import async_pool
from async_websocket import async_websocket

load_dotenv()

"""
Generic entry for the beginning scan session
"""

# Markets can be introduced from here
markets = [
    os.getenv('BIT'),
    os.getenv('BFN'),
    os.getenv('COI'),
]


async def entry():
    """
    Proxy entry point from main to
    initiate all market coroutines
    :return: void
    """
    # Create connection pool
    pool = await async_pool.create_pool()
    # Dynamically gather each configured market
    await asyncio.gather(
        *[initiate(x, pool) for x in markets]
    )


async def initiate(market: str, pool):
    """
    Spins up the websocket entry point
    :param market:
    :param pool:
    :return:
    """
    await async_websocket.initiate_socket(market, pool)


if __name__ == '__main__':
    asyncio.run(entry())
