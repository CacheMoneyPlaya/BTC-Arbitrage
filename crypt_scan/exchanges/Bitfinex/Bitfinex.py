import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_parser
from exchanges.BaseExchange import BaseExchange


class Bitfinex(BaseExchange):

    """
    ID|PRICE|ORDER_COUNT|VOLUME

     [256,
         [ 36624,
           3,
           0.64041059
         ]
     ]
    """

    EXCHANGE = os.getenv('BFN')
    COLOR = os.getenv(EXCHANGE + '_C')

    load_dotenv(dotenv_path=BaseExchange.env_path)

    def __init__(self, message, pool):
        self.message = message
        self.pool = pool

    def is_valid(self) -> bool:
        return (len(self.message[1])) == 3 and self.message[1][1]

    def parse(self) -> dict:

        self.isolate_order()

        self.load = self.build_load(
            self.get_price(),
            self.get_quantity(),
            self.get_side(),
            self.EXCHANGE,
            self.get_order_value()
        )

        print('%s %s %s %s' % (fg('white'), bg(self.COLOR), self.load, attr('reset')))

        return self.load

    def get_price(self) -> int:
        """
         Returns price
        :return int:
        """
        return self.order[0]

    def get_quantity(self) -> int:
        """
        Returns absolute polarity of order volume
        :return int:
        """
        return abs(self.order[2])

    def get_side(self) -> str:
        """
        Determines the Bitfinex order polarity
        :return string:
        """
        return BaseExchange.SELL if self.order[2] < 0 else BaseExchange.BUY

    def get_order_value(self) -> float:
        """
        Determines the Bitmex order value, slims down query
        :return float:
        """
        order_value = round(float(self.order[0]) * abs(float(self.order[2])), 2)
        return order_value

    def isolate_order(self) -> None:
        self.order = self.message[1]
