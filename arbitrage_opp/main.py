from dotenv import load_dotenv
from scanner import scanner
import time
load_dotenv()

"""
Generic entry for the beginning scan session
"""
def entry():
    """
    Proxy entry point from main
    :return: void
    """
    while True:
        scanner.execute_match_search()
        time.sleep(1)

if __name__ == '__main__':
    entry()
