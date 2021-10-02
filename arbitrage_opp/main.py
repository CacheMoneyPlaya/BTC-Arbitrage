from dotenv import load_dotenv
from scanner import scanner
load_dotenv()

"""
Generic entry for the beginning scan session
"""
def entry():
    """
    Proxy entry point from main
    :return: void
    """
    scanner.execute_match_search()

if __name__ == '__main__':
    entry()
