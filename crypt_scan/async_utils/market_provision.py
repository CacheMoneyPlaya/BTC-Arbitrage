import os
import json
import aiohttp
from pathlib import Path
import dotenv
import logging

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
WAIT_TIMEOUT = 20
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def get_bit_provisions(load):
    return [(str(i), str(d.get('tickSize'))) for i, d in enumerate(load) if d['symbol'] == 'XBTUSD'][0]


async def provision_market(market: str):
    if market == os.getenv('BIT'):
        try:
            await provision_bit()
        except:
            logging.info('Unable to determine BIT provision, defaulting to previous')
        else:
            logging.info('BIT Provisioned')
    else:
        return


async def provision_bit():
    async with aiohttp.ClientSession() as s:
        async with s.get(os.getenv('BIT_PROV')) as r:
            prov = get_bit_provisions(json.loads(await r.text()))
            os.environ["BIT_IDX"], os.environ["BIT_TICKSIZE"] = prov
            set_env('BIT_IDX', os.environ["BIT_IDX"])
            set_env('BIT_TICKSIZE', os.environ["BIT_TICKSIZE"])



def set_env(key: str, value: str):
    dotenv.set_key(dotenv_file, key, value)
