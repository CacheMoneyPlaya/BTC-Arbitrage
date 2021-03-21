import os
import json
import asyncio
from pathlib import Path
from websockets import connect
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_provision
from async_database import market_handler

"""
Timeout defined WS
"""
WAIT_TIMEOUT = 20


async def initiate_socket(market: str, pool):
    handle = getattr(market_handler, market.lower()+'_handler')
    await market_provision.provision_market(market)
    async with connect(os.getenv(market+'_WS')) as ws:
        await ws.send(os.getenv(market+'_SUB'))
        while True:
            try:
                response = await asyncio.wait_for(ws.recv(), WAIT_TIMEOUT)
                raw_msg = json.loads(response)
                handle(raw_msg)
                print('%s %s %s %s' % (fg('white'), bg(os.getenv(market + '_C')), raw_msg, attr('reset')))
                print('\n')
            except:
                exit()

