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


 foreignNotional: USD value of order
 homeNotional: Order size in bitcoin
 grossValue: Order size in sat(e-8 of a Bitcoin each)

 In this response example we have a sell order for ~$3.6k
 and the volume of bitcoin is 0.0594..


BITFINEX:

 {[
    1, Channel
    'te', Channel Id
    [
      642062244, Trade Id
      1615673602349, Millisecond Timestamp
      0.12234142, ±Amount
      60883 $Price
    ]
  ]}

 The order side can be determined determined with a
 prefixed polarity against the amount

COINBASE:

 {
  'type': 'ticker',
  'sequence': 22679094330,
  'product_id': 'BTC-USD',
  'price': '60979.05',
  'open_24h': '57180.23',
  'volume_24h': '21741.25136546',
  'low_24h': '56083.74',
  'high_24h': '61788.45',
  'volume_30d': '727613.57414185',
  'best_bid': '60979.04',
  'best_ask': '60979.05',
  'side': 'buy',
  'time': '2021-03-13T22:24:56.708861Z',
  'trade_id': 144598885,
  'last_size': '0.01471539'
 }
