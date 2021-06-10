import os
from colored import fg, bg, attr
from exchanges.Bitmex import Bitmex
from exchanges.Bitfinex import Bitfinex
from exchanges.Coinbase import Coinbase
from async_utils import market_parser as mp

def validate_bit(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        module = Bitmex(message, pool)
        if module.is_valid():
            return func(module)
    return wrap


def validate_coi(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        module = Coinbase(message, pool)
        if module.is_valid():
            return func(module)
    return wrap


def validate_bfn(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        module  = Bitfinex(message, pool)
        if module.is_valid():
            return func(module)
    return wrap


@validate_bit
def bit_handler(bit_module: Bitmex):
    load = bit_module.parse()


@validate_coi
def coi_handler(coi_module: Coinbase):
    loads = coi_module.parse()


@validate_bfn
def bfn_handler(bfn_module: Bitfinex):
    load = bfn_module.parse()
