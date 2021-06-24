import os

"""
Parent class that all exchanges can
inherit from, will increase in size
over dev time
"""
class BaseExchange():

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
