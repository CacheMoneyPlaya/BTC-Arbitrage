import urllib.request
from dotenv import load_dotenv
from pathlib import Path
import os
import aiohttp
import json


env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)


def bit_parser(message: dict):
    print(message)
    exit()
# def bfn_parser(message: dict):
#
# def coi_parser(message: dict):




