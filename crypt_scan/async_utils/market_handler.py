from async_utils import market_parser as mp
from colored import fg, bg, attr
import os


def validate_bit(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        if message.get('action') == 'insert':
            return func(message.get('data'), pool, market)
    return wrap


def validate_coi(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        volume = float(message.get('changes')[0][2])
        if volume != 0.0:
            return func(*message.get('changes'), pool, market)
    return wrap


def validate_bfn(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool, market):
        print(message)
        return func(message[1], pool, market)
    return wrap


# ASSET|PRICE|QTY|SIDE|EXCHANGE|TIMESTAMP


@validate_bit
def bit_handler(message: dict, pool, market: str):
    # Run Parser
    # print('%s %s %s %s' % (fg('white'), bg(os.getenv(market + '_C')), message, attr('reset')))
    # print('\n')
    # Need to handle multiple
    messages = mp.bit_parser(message, market)


@validate_coi
def coi_handler(message: dict, pool, market: str):
    # Run Parser
    # print('%s %s %s %s' % (fg('white'), bg(os.getenv(market + '_C')), message, attr('reset')))
    # print('\n')
    messages = mp.coi_parser(message, market)


@validate_bfn
def bfn_handler(message: str, pool, market: str):
    # Run Parser
    # print('%s %s %s %s' % (fg('white'), bg(os.getenv(market + '_C')), message, attr('reset')))
    # print('\n')
    print('.')


def oder_book_insert():
    print('test_order_book_insert')
    # Pass pool client
    # Call db handler
