def build_load(*args):
    """
    Stardardised dict format must
    be in order:
    PRICE|QTY|SIDE|EXCHANGE
    :param func:
    :return:
    """
    return {
        'asset': 'BTC',
        'price': args[0],
        'quantity': args[1],
        'side': args[2],
        'exchange': args[3],
    }
