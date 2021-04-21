from async_utils import market_parser



def validate_bit(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool):
        if message.get('action') == 'insert':
            return func(message.get('data'), pool)
    return wrap


@validate_bit
def bit_handler(message: dict, pool):
    # Run Parser
    # Run db entry
    print(message)


def coi_handler(message: str, pool):
    # Run Parser
    print('test_coi')


def bfn_handler(message: str, pool):
    # Run Parser
    print('test_bfn')


def oder_book_insert():
    print('test_order_book_insert')
    # Pass pool client
    # Call db handler

