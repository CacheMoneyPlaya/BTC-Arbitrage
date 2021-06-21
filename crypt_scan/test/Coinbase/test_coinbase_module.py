import sys
sys.path.append('.')
from exchanges.Coinbase import Coinbase
import pytest

class TestCoinbase():

    coi_module = None
    coi_msg = None


    @classmethod
    def setup_class(cls):
        cls.coi_msg = {'type': 'l2update', 'product_id': 'BTC-USD', 'changes': [['buy', '40143.01', '0.26000000']], 'time': '2021-06-15T22:29:57.478518Z'}
        cls.coi_module = Coinbase(cls.coi_msg, None)
        cls.coi_module.isolate_order()


    @classmethod
    def tearDownClass(cls):
        cls.coi_module = None
        cls.coi_msg = None


    def test_coinbase_instance(self):
        assert self.coi_module.message == self.coi_msg


    def test_can_get_price(self):
        assert self.coi_module.get_price() == '40143.01'


    def test_can_get_quantity(self):
        assert self.coi_module.get_quantity() == '0.26000000'


    def test_can_validate(self):
        assert self.coi_module.is_valid() == True


    def test_can_get_side(self):
        assert self.coi_module.get_side() == 'buy'
