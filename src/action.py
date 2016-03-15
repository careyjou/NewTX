''' operations done in main.py are placed here for making the strategy concise '''
from T4 import *
from datetime import datetime
import g

def buy(price,amount):
    if buy_api(price,amount) == True:
        g.lot +=1
        g.buy_list.append(price)

def sell(price):
    if sell_api(price,amount) == True:
        g.lot -=1
        g.sell_list.append(price)

def withdraw_or_not(price):
    # TODO
    return False

def withdraw(price):
    if g.lot < 0:
        g.lot +=1
    elif g.lot > 0:
        g.lot -=1

def print_status():
    print("# -- " + str(datetime.now()) + " -- #")
    print "Remaining g.lot(s) = ", g.lot
    if g.lot > 0:
        print "buy_list = " + str(g.buy_list)
    elif g.lot < 0:
        print "sell_list = " + str(g.sell_list)
    print
