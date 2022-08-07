import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

def get_connection():
    return psycopg2.connect(
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PASS'),
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT'),
            database=os.getenv('PG_DATABASE')
        )



def get_cursor(connection):
    return connection.cursor()

