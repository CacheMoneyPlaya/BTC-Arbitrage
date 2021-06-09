import urllib.request
from dotenv import load_dotenv
from pathlib import Path
import os
import aiohttp
import json
import math
from async_utils import bit_utils
from colored import fg, bg, attr


env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)
# ASSET|PRICE|QTY|SIDE|EXCHANGE|TIMESTAMP

def bit_parser(message: dict, exchange: str):
    """
    Bitmex provides multiple orders
    per message and requies us to reverse
    engineer the price level per grouping
    :return: void
    """

    loads = []
    for m in message:
        price = bit_utils.get_price(m.get('id'))
        quantity = bit_utils.get_quantity(price, m.get('size'))

        loads.append(
            build_load(
                price,
                quantity,
                m.get('side'),
                exchange
            )
        )

    for l in loads: print('%s %s %s %s' % (fg('white'), bg(os.getenv(exchange + '_C')), l, attr('reset')))


def coi_parser(message: list, exchange: str):
    """
    Coin base parser, no funny stuff
    needed
    :return: void
    """
    load = build_load(
        message[1],
        message[2],
        message[0],
        exchange
    )

    print('%s %s %s %s' % (fg('white'), bg(os.getenv(exchange + '_C')), load, attr('reset')))


def bfn_parser(message: dict, exchange):

    load = build_load(
        message[0],
        abs(message[2]),
        'sell' if message[2] < 0 else 'buy',
        exchange
    )

    print('%s %s %s %s' % (fg('white'), bg(os.getenv(exchange + '_C')), load, attr('reset')))


def build_load(*args):
    """
    Stardardised dict format must
    be in order:
    PRICE|QTY|SIDE|EXCHANGE
    :param func:
    :return:
    """
    return {
        'asset': 'BTC',
        'price': args[0],
        'quantity': args[1],
        'side': args[2],
        'exchange': args[3],
    }
