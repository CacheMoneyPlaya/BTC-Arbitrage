from postgres_connection import postgres_connection as pc
import psycopg2

def execute_session():
   try:
       connection = pc.get_connection()
       cursor = pc.get_cursor(connection)
       cursor.execute(build_arbitrage_query())
       records = cursor.fetchall()
       for row in records:
           print(row, "\n")
   except(Exception, psycopg2.Error) as error:
       print(error)
   finally:
        if connection:
            cursor.close()
            connection.close()

def build_arbitrage_query():
   return """SELECT
    buy_side.id buy_id,
    sell_side.id as sell_id,
    ((buy_side.price * LEAST(buy_side.size, sell_side.size)) - (sell_side.price * LEAST(buy_side.size, sell_side.size))) AS price_spread,
    sell_side.exchange as exchange_from,
    buy_side.exchange AS exchange_to,
    LEAST(buy_side.size, sell_side.size) as max_size
    FROM buy_side, sell_side
    WHERE (buy_side.price * LEAST(buy_side.size, sell_side.size)) > (sell_side.price * LEAST(buy_side.size, sell_side.size))
    AND ((buy_side.price * LEAST(buy_side.size, sell_side.size)) - (sell_side.price * LEAST(buy_side.size, sell_side.size))) > ((0.0025 * sell_side.price * LEAST(buy_side.size, sell_side.size)) + (0.0025 * buy_side.price * LEAST(buy_side.size, sell_side.size)))
    AND buy_side.exchange <> sell_side.exchange
    AND buy_side.timestamp > NOW() - INTERVAL '5 SECONDS'
    AND sell_side.timestamp > NOW() - INTERVAL '5 SECONDS';"""
