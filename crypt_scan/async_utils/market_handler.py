import os
from colored import fg, bg, attr
from exchanges.ExchangeFactory import ExchangeFactory
from async_utils import market_parser as mp


def validate_bit(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        module = ExchangeFactory.resolve_bitmex(message, pool)
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
        module = ExchangeFactory.resolve_coinbase(message, pool)
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
        module = ExchangeFactory.resolve_bitfinex(message, pool)
        if module.is_valid():
            return func(module)
    return wrap


@validate_bit
def bit_handler(bit_module: ExchangeFactory):
    load = bit_module.parse()


@validate_coi
def coi_handler(coi_module: ExchangeFactory):
    loads = coi_module.parse()


@validate_bfn
def bfn_handler(bfn_module: ExchangeFactory):
    load = bfn_module.parse()
