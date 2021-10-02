from postgres_connection import postgres_connection as pc

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
    return "select * from price_points"
