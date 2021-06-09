Three main exchange websockets being used at the moment:

BITMEX:

 {
    'table': 'orderBookL2_25',
    'action': 'update',
    'data': [
        {
            'symbol': 'XBTUSD',
            'id': 8794132050,
            'side': 'Buy',
            'size': 260234
        },
        {
            'symbol': 'XBTUSD',
            'id': 8794134150,
            'side': 'Buy',
            'size': 10000
        }
     ]
 }

 ID = (100000000 * symbolIdx) - (price / instrumentTickSize)
 price = ((100000000 * symbolIdx) - ID) * instrumentTickSize

 {'symbol': 'XBTUSD', 'id': 8796452050, 'side': 'Sell', 'size': 18000, 'price': 35479.5}

 Size is price


 foreignNotional: USD value of order
 homeNotional: Order size in bitcoin
 grossValue: Order size in sat(e-8 of a Bitcoin each)

 In this response example we have a sell order for ~$3.6k
 and the volume of bitcoin is 0.0594..


BITFINEX:

 [256, [36624, 3, 0.64041059]]
 channelid, price, count, total (±)

 [12170, [36650, 1, -0.0042]]

 total of 1 order for the sale of 0.0042BTC at 36650 USD

 The order side can be determined with a
 prefixed polarity against the amount

COINBASE:

[side, price, size]


172.25.40.162
172.31.46.113
172.26.246.156
5432
postgres



STORAGE:
ASSET|PRICE|QTY|SIDE|EXCHANGE|TIMESTAMP
