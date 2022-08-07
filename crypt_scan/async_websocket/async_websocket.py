import os
import json
import asyncio
from pathlib import Path
from websockets import connect
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_provision, market_handler
import time

"""
Timeout defined WS
"""
WAIT_TIMEOUT = 20


async def initiate_socket(market: str, pool):
    """
    Initiates a specified market websocket subscription
    :param market:
    :param pool:
    :return:
    """
    count = 0
    # Configure market data handler
    handle = getattr(market_handler, market.lower()+'_handler')
    # Provision the market if required
    await market_provision.provision_market(market)
    # Initiate the market websocket subscription
    async with connect(os.getenv(market+'_WS')) as ws:
        await ws.send(os.getenv(market+'_SUB'))
        t0 = time.time()
        while True:
            try:
                t1 = time.time()
                # Simple filter of intial connection messages
                response = await asyncio.wait_for(ws.recv(), WAIT_TIMEOUT)
                if t1-t0 > 5:
                    raw_msg = json.loads(response)
                    await handle(raw_msg, pool, market)
            except Exception as e:
                print(str(e))
