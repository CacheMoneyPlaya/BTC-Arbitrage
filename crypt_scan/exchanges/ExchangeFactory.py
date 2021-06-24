from exchanges.Coinbase.Coinbase import Coinbase
from exchanges.Bitmex.Bitmex import Bitmex
from exchanges.Bitfinex.Bitfinex import Bitfinex


class ExchangeFactory(object):

    @classmethod
    def resolve_coinbase(cls, message, pool) -> Coinbase:
        return Coinbase(message, pool)

    @classmethod
    def resolve_bitfinex(cls, message, pool) -> Bitfinex:
        return Bitfinex(message, pool)

    @classmethod
    def resolve_bitmex(cls, message, pool) -> Bitmex:
        return Bitmex(message, pool)
