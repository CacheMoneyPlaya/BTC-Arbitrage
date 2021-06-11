
A BTCUSD arbitrage bot using Bitfinex, Bitmex and Coinbase (Soon to introduce Binance)

Utilizes asyncio to make heavy use of coroutines in sync with asyncpg


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


BITFINEX:

 [256, [36624, 3, 0.64041059]]

COINBASE:

[side, price, size]

https://user-images.githubusercontent.com/39480577/121440074-19741680-c97f-11eb-9d36-68a688403a42.mp4
