import os
from pathlib import Path
from dotenv import load_dotenv
from colored import fg, bg, attr
from exchanges.BaseExchange import BaseExchange

class Bitmex(BaseExchange):

        # """
        #  {
        #     'table': 'orderBookL2_25',
        #     'action': 'insert',
        #     'data': [
        #         {
        #             'symbol': 'XBTUSD',
        #             'id': 8794132050,
        #             'side': 'Buy',
        #             'size': 260234
        #         },
        #         {
        #             'symbol': 'XBTUSD',
        #             'id': 8794134150,
        #             'side': 'Buy',
        #             'size': 10000
        #         }
        #      ]
        #  }
        # """

    IDX = float(os.getenv('BIT_IDX'))
    TICK_SIZE = float(os.getenv('BIT_TICKSIZE'))
    EXCHANGE = os.getenv('BIT')
    BIT_PRICE_RATIO = float(os.getenv('BIT_PRICE_RATIO'))
    COLOR = os.getenv(EXCHANGE + '_C')

    load_dotenv(dotenv_path=BaseExchange.env_path)


    def __init__(self, message, pool):
        self.message = message
        self.pool = pool


    def is_valid(self) -> bool:
        return self.message.get('action') == BaseExchange.INSERT


    def parse(self) -> None:
        self.isolate_orders()
        self.loads = []

        for order in self.orders:

            price = self.get_price(order)
            quantity = self.get_quantity(order, price)
            side = self.get_side(order)

            self.loads.append(
                self.build_load(
                    price,
                    quantity,
                    side,
                    self.EXCHANGE
                )
            )

        for l in self.loads: print('%s %s %s %s' % (fg('white'), bg(self.COLOR), l, attr('reset')))


    def get_price(self, order: dict) -> int:
        """
         Reverse engineers the order
         price level
        :return int:
        """
        return ((self.BIT_PRICE_RATIO * self.IDX) - order.get('id')) * self.TICK_SIZE


    def get_quantity(self, order, price) -> int:
        """
        Calculates the BITMEX order quantity
        :return int:
        """
        return round(order.get('size')/price, 5)



    def get_side(self, order) -> str:
        """
        Determines the BITMEX order side
        :return int:
        """
        return order.get('side')

    def isolate_orders(self) -> None:
        self.orders = self.message.get('data')
