import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from exchanges.BaseExchange import BaseExchange


class Coinbase(BaseExchange):

    """
    MESSAGE STRUCTURE:
     [
        side,
        price,
        size
     ]
    """
    EXCHANGE = os.getenv('COI')
    COLOR = os.getenv(EXCHANGE + '_C')

    load_dotenv(dotenv_path=BaseExchange.env_path)

    def __init__(self, message, pool):
        self.message = message
        self.pool = pool

    def is_valid(self) -> bool:
        volume = float(self.message.get('changes')[0][2])
        return volume != 0.0

    def parse(self) -> None:

        self.isolate_order()
        self.load = self.build_load(
            self.get_price(),
            self.get_quantity(),
            self.get_side(),
            self.EXCHANGE,
            self.get_order_value(),
        )

        print('%s %s %s %s' % (fg('white'), bg(self.COLOR), self.load, attr('reset')))

        return self.load

    def get_price(self) -> int:
        """
         Returns price
        :return int:
        """
        return self.order[1]

    def get_quantity(self) -> int:
        """
        Returns absolute polarity of order volume
        :return int:
        """
        return self.order[2]

    def get_side(self) -> str:
        """
        Determines the Coinbase order polarity
        :return string:
        """
        return self.order[0].upper()

    def get_order_value(self) -> float:
        """
        Determines the Coinbase order value, slims down query
        :return float:
        """
        order_value = round((float(self.order[2]) * float(self.order[1])), 2)
        return order_value

    def isolate_order(self) -> None:
        self.order = self.message.get('changes')[0]
