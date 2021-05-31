from async_utils import market_parser as mp



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


def validate_coi(func):
    """
    Decorator that filters out incorrect
    actions and payloads
    :param func:
    :return:
    """
    def wrap(message, pool):
        if message.get('changes'):
            return func(*message.get('changes'), pool)
    return wrap


# def validate_bfn(func):
#     """
#     Decorator that filters out incorrect
#     actions and payloads
#     :param func:
#     :return:
#     """
#     def wrap(message, pool):
#         if len()
#         print(message)
#     return wrap


@validate_bit
def bit_handler(message: dict, pool):
    # Run Parser
    mp.bit_parser()
    print(message)
    # Run db entry


@validate_coi
def coi_handler(message: dict, pool):
    # Run Parser
    print('test_coi')
    print(message)

# @validate_bfn
def bfn_handler(message: str, pool):
    # print(message)
    # Run Parser
    print('test_bfn')


def oder_book_insert():
    print('test_order_book_insert')
    # Pass pool client
    # Call db handler
