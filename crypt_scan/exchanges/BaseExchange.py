import os
from pathlib import Path

"""
Parent class that all exchanges can
inherit from, will increase in size
over dev time
"""


class BaseExchange():

    env_path = Path('../') / '.env'
    SELL = 'SELL'
    BUY = 'BUY'
    UPDATE = 'update'
    INSERT = 'insert'

    def build_load(self, *args) -> dict:
        """
        Stardardised dict format must
        be in order:
        PRICE|QTY|SIDE|EXCHANGE|ORDER_VALUE
        :param func:
        :return:
        """
        return {
            'asset': 'BTC',
            'exchange': args[3],
            'side': args[2],
            'price': float(args[0]),
            'quantity': float(args[1]),
            'order_value': float(args[4])
        }
