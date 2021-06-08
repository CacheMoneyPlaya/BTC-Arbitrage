import urllib.request
from dotenv import load_dotenv
from pathlib import Path
import os
import aiohttp
import json
import math


env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

# ASSET|PRICE|QTY|SIDE|EXCHANGE|TIMESTAMP
def bit_parser(message: dict, exchange: str):

    loads = []
    for m in message:
        price = ((100000000 * float(os.getenv(exchange+'_IDX'))) - m.get('id')) * float(os.getenv(exchange+'_TICKSIZE'))
        loads.append(
            build_load(
                price,
                round(m.get('size')/price, 5),
                m.get('side'),
                exchange
            )
        )

    print(loads)


def coi_parser(message: list, exchange: str):

    load = build_load(
        message[1],
        message[2],
        message[0],
        exchange
    )


def bfn_parser(message: dict, exchange):
    return True



def build_load(*args):

    return {
        'asset': 'BTC',
        'price': args[0],
        'quantity': args[1],
        'side': args[2],
        'exchange': args[3],
    }
