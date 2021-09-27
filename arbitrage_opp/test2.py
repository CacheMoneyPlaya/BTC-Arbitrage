from datetime import datetime
import os

print(os.getcwd())
myFile = open('arbitrage_opp/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))
