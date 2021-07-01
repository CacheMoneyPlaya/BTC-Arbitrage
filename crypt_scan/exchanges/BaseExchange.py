import os
from pathlib import Path

"""
Parent class that all exchanges can
inherit from, will increase in size
over dev time
"""
class BaseExchange():

    env_path = Path('../') / '.env'
    SELL = 'sell'
    BUY = 'buy'
    UPDATE = 'update'
    INSERT = 'insert'

    def build_load(self, *args) -> dict:

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
