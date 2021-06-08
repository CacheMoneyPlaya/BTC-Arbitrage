import os
import json
import aiohttp
import dotenv
import logging

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
WAIT_TIMEOUT = 20
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

async def provision_market(market: str):
    """
    Provisions the supplied market if required
    :param market:
    :return:
    """
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
    """
    Fetches the BIT socket subscription credentials
    :return:
    """
    async with aiohttp.ClientSession() as s:
        async with s.get(os.getenv('BIT_PROV')) as r:
            prov = get_bit_provisions(json.loads(await r.text()))
            os.environ["BIT_IDX"], os.environ["BIT_TICKSIZE"] = prov

            #Sets the BIT socket subscription credentials in env
            set_env('BIT_IDX', os.environ["BIT_IDX"])
            set_env('BIT_TICKSIZE', os.environ["BIT_TICKSIZE"])


def get_bit_provisions(load):
    """
    Filters out the BIT
    :param load:
    :return:
    """
    # Temporary override as per https://www.bitmex.com/app/wsAPI#OrderBookL2
    # str(d.get('tickSize'))
    return [(str(i), '0.01') for i, d in enumerate(load) if d['symbol'] == 'XBTUSD'][0]


def set_env(key: str, value: str):
    """
    Generic environment provisioner
    :param key:
    :param value:
    :return:
    """
    dotenv.set_key(dotenv_file, key, value)
