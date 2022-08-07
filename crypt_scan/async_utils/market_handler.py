import os
from colored import fg, bg, attr
from exchanges.ExchangeFactory import ExchangeFactory
from async_utils import market_parser as mp
from async_database import async_pool as adp
from async_redis import async_pool as arp
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



# @validate_bit
# async def bit_handler(bit_module: ExchangeFactory, pool):
#     loads = bit_module.parse()
#     async with pool.acquire() as con:
#         list([await async_pool.insert_order(con, order, 'BIT') for order in loads])
#
#
# @validate_coi
# async def coi_handler(coi_module: ExchangeFactory, pool):
#     load = coi_module.parse()
#     async with pool.acquire() as con:
#         await async_pool.insert_order(con, load, 'COI')
#
#
# @validate_bfn
# async def bfn_handler(bfn_module: ExchangeFactory, pool):
#     load = bfn_module.parse()
#     async with pool.acquire() as con:
#         await async_pool.insert_order(con, load, 'COI')


@validate_bit
async def bit_handler(bit_module: ExchangeFactory, pool):
    loads = bit_module.parse()
    list([await arp.insert_order(pool, order) for order in loads])


@validate_coi
async def coi_handler(coi_module: ExchangeFactory, pool):
    load = coi_module.parse()
    await arp.insert_order(pool, load)



@validate_bfn
async def bfn_handler(bfn_module: ExchangeFactory, pool):
    load = bfn_module.parse()
    await arp.insert_order(pool, load)
