import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_parser

class Coinbase():

    env_path = Path('../') / '.env'
    UPDATE = 'update'
    CONST = 1e8
    EXCHANGE = os.getenv('COI')
    SELL = 'sell'
    BUY = 'buy'

    load_dotenv(dotenv_path=env_path)


    def __init__(self, message, pool):
        self.message = message
        self.pool = pool


    def is_valid(self):
        volume = float(self.message.get('changes')[0][2])
        return volume != 0.0


    def parse(self):
        self.isolate_order()
        load = market_parser.build_load(
                self.get_price(),
                self.get_quantity(),
                self.get_side(),
                self.EXCHANGE
            )

        print('%s %s %s %s' % (fg('white'), bg(os.getenv(self.EXCHANGE + '_C')), load, attr('reset')))


    def get_price(self):
        """
         Returns price
        :return int:
        """
        return self.order[1]


    def get_quantity(self):
        """
        Returns absolute polarity of order volume
        :return int:
        """
        return self.order[2]


    def get_side(self):
        """
        Determines the Coinbase order polarity
        :return string:
        """
        return self.order[0]

    def isolate_order(self):
        self.order = self.message.get('changes')[0]
