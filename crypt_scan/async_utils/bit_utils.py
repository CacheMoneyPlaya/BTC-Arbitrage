import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

CONST = 1e8
IDX = float(os.getenv('BIT_IDX'))
TICK_SIZE = float(os.getenv('BIT_TICKSIZE'))

def get_price(id: int):
    """
     Reverse engineers the order
     price level
    :param id:
    :return:
    """
    return ((CONST * IDX) - id) * TICK_SIZE

def get_quantity(price: int, size: int):
    """
    Calculates the BITMEX order quantity
    :param price, size:
    :return int:
    """
    return round(size/price, 5)
