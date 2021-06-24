import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_parser


class Bitfinex():

    """
    ID|PRICE|ORDER_COUNT|VOLUME

     [256,
         [ 36624,
           3,
           0.64041059
         ]
     ]
    """

    env_path = Path('../') / '.env'
    UPDATE = 'update'
    CONST = 1e8
    EXCHANGE = os.getenv('BFN')
    SELL = 'sell'
    BUY = 'buy'

    load_dotenv(dotenv_path=env_path)

    def __init__(self, message, pool):
        self.message = message
        self.pool = pool

    def is_valid(self) -> bool:
        return (len(self.message[1])) == 3 and self.message[1][1]

    def parse(self) -> None:

        self.isolate_order()
        self.load = market_parser.build_load(
            self.get_price(),
            self.get_quantity(),
            self.get_side(),
            self.EXCHANGE
        )

        print('%s %s %s %s' % (fg('white'), bg(
            os.getenv(self.EXCHANGE + '_C')), self.load, attr('reset')))

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
        return self.SELL if self.order[2] < 0 else self.BUY

    def isolate_order(self) -> None:
        self.order = self.message[1]
