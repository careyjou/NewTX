''' operations done in main.py are placed here for making the strategy concise '''
from T4 import *
from datetime import datetime
import g

def buy(price):
    ret = buy_api(price)
    if ret == True:
        g.lot +=1
        g.buy_list.append(price)
    return ret

def sell(price):
    ret = sell_api(price)
    if ret == True:
        g.lot -=1
        g.sell_list.append(price)
    return ret

def withdraw_or_not(price):
    # TODO
    return False

def withdraw(price):
    if g.lot < 0:
        ret = buy(price)
        if ret == True: g.lot +=1
        return ret
    elif g.lot > 0:
        ret = sell(price)
        if ret == True: g.lot -=1
        return ret
    else:
        print "You have nothing to offset, Mr. Loser."

def print_status():
    print("# -- " + str(datetime.now()) + " -- #")
    print "Remaining g.lot(s) = ", g.lot
    if g.lot > 0:
        print "buy_list = " + str(g.buy_list)
    elif g.lot < 0:
        print "sell_list = " + str(g.sell_list)
    print
