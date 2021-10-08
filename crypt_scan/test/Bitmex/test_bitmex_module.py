import pytest
from exchanges.Bitmex.Bitmex import Bitmex
import sys
sys.path.append('.')


class TestBitmex():

    bit_module = None
    bit_msg = None

    BUY = 'BUY'
    SELL = 'SELL'

    @classmethod
    def setup_class(cls):
        cls.bit_msg = {'table': 'orderBookL2_25', 'action': 'update', 'data': [
            {'symbol': 'XBTUSD', 'id': 8796818050, 'side': 'Buy', 'size': 443900}]}
        cls.bit_module = Bitmex(cls.bit_msg, None)
        cls.order = cls.bit_msg.get('data')[0]

    @classmethod
    def tearDownClass(cls):
        cls.bit_module = None
        cls.bit_msg = None

    def test_bitnbase_instance(self):
        assert self.bit_module.message == self.bit_msg

    def test_can_get_price(self):
        assert self.bit_module.get_price(self.order) == 31819.5

    def test_can_get_quantity(self):
        assert self.bit_module.get_quantity(self.order, 31819.5) == 13.95056

    def test_can_validate(self):
        assert self.bit_module.is_valid() == False

    def test_can_get_side(self):
        assert self.bit_module.get_side(self.order) == self.BUY

    def test_can_isolate_order(self):
        self.bit_module.isolate_orders()
        assert self.bit_module.orders == [self.order]
