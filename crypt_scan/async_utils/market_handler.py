import os
from colored import fg, bg, attr
from exchanges.ExchangeFactory import ExchangeFactory
from async_utils import market_parser as mp
from datetime import datetime


def validate_bit(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    async def wrap(message, pool, market):
        module = ExchangeFactory.resolve_bitmex(message, pool)
        if module.is_valid():
            return await func(module, pool)
    return wrap


def validate_coi(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    async def wrap(message, pool, market):
        module = ExchangeFactory.resolve_coinbase(message, pool)
        if module.is_valid():
            return await func(module, pool)
    return wrap


def validate_bfn(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    async def wrap(message, pool, market):
        module = ExchangeFactory.resolve_bitfinex(message, pool)
        if module.is_valid():
            return await func(module, pool)
    return wrap


@validate_bit
async def bit_handler(bit_module: ExchangeFactory, pool):
    load = bit_module.parse()
    async with pool.acquire() as con:
        await con.execute('''INSERT INTO price_points VALUES('BIT', 1, 2, '1999-01-08 04:05:06')''')
    # Set in postgres via pool


@validate_coi
async def coi_handler(coi_module: ExchangeFactory, pool):
    loads = coi_module.parse()
    async with pool.acquire() as con:
        await con.execute('''INSERT INTO price_points VALUES('COI', 1, 2, '1999-01-08 04:05:06')''')
    # Set in postgres via pool


@validate_bfn
async def bfn_handler(bfn_module: ExchangeFactory, pool):
    load = bfn_module.parse()
    async with pool.acquire() as con:
        await con.execute('''INSERT INTO price_points VALUES('BFN', 1, 2, '1999-01-08 04:05:06')''')
    # Set in postgres via pool
