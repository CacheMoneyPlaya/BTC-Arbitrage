import sys
sys.path.append('.')
from exchanges.Coinbase import Coinbase
import unittest

class TestCoinbase(unittest.TestCase):

    TEST_MESSAGE = None
    coi_mod = None

    @classmethod
    def setUpClass(cls):
        cls.coi_msg = {'type': 'l2update', 'product_id': 'BTC-USD', 'changes': [['buy', '40143.01', '0.26000000']], 'time': '2021-06-15T22:29:57.478518Z'}
        cls.coi_mod = Coinbase(cls.coi_msg, None)
        cls.coi_mod.isolate_order()


    @classmethod
    def tearDownClass(cls):
        cls.coi_mod = None

    def test_coinbase_instance(self):
        self.assertEqual(self.coi_mod.message, self.coi_msg)


    def test_can_get_price(self):
        self.assertEqual(self.coi_mod.get_price(), '40143.01')


    def test_can_get_quantity(self):
        self.assertEqual(self.coi_mod.get_quantity(), '0.26000000')


    def test_can_validate(self):
        self.assertEqual(self.coi_mod.is_valid(), True)


    def test_can_get_side(self):
        self.assertEqual(self.coi_mod.get_side(), 'buy')


if __name__ == '__main__':
    unittest.main()
