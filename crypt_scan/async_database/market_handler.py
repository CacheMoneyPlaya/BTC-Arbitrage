def bit_handler(message: str, pool):
    # Run Parser
    print(message['data'])
    print('test_bit')
    # {'table': 'orderBookL2_25', 'action': 'update',
    #  'data': [{'symbol': 'XBTUSD', 'id': 8794100550, 'side': 'Buy', 'size': 4721384}]}


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

