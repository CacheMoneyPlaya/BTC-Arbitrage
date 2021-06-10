import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from async_utils import market_parser

class Bitmex():

    env_path = Path('../') / '.env'
    UPDATE = 'update'
    CONST = 1e8
    IDX = float(os.getenv('BIT_IDX'))
    TICK_SIZE = float(os.getenv('BIT_TICKSIZE'))
    EXCHANGE = os.getenv('BIT')

    load_dotenv(dotenv_path=env_path)


    def __init__(self, message, pool):
        self.message = message
        self.pool = pool


    def is_valid(self):
        return self.message.get('action') == self.UPDATE


    def parse(self):
        self.isolate_orders()

        for order in self.orders:
            loads = []
            price = self.get_price(order)
            quantity = self.get_quantity(order, price)
            side = self.get_side(order)

            loads.append(
                market_parser.build_load(
                    price,
                    quantity,
                    side,
                    self.EXCHANGE
                )
            )

        for l in loads: print('%s %s %s %s' % (fg('white'), bg(os.getenv(self.EXCHANGE + '_C')), l, attr('reset')))


    def get_price(self, order: dict):
        """
         Reverse engineers the order
         price level
        :return int:
        """
        return ((self.CONST * self.IDX) - order.get('id')) * self.TICK_SIZE


    def get_quantity(self, order, price):
        """
        Calculates the BITMEX order quantity
        :return int:
        """
        return round(order.get('size')/price, 5)



    def get_side(self, order):
        """
        Determines the BITMEX order side
        :return int:
        """
        return order.get('side')

    def isolate_orders(self):
        self.orders = self.message.get('data')
