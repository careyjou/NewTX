''' operations done in main.py are placed here for making the strategy concise '''
'''
Note that the functions of sell/buy/withdraw below are NOT guaranteed to succeed because of using IOC rather than ROD.
You have to check whether it succeeds or not by checking the returned TRUE/FALSE
'''
from T4py import *
from datetime import datetime
import g

def buy(price):
    old_lot = query_lot()
    print 'old lot = ' + str(old_lot)
    ret = buy(price, g.FUTURE_ID, lot_type = " ")
    if ret == None:
        return False

    new_lot = query_lot()
    print 'new lot = ' + str(new_lot)
    if new_lot < (old_lot + 1):
        return False
    else:
        return True

def sell(price):
    old_lot = query_lot()
    print 'old lot = ' + str(old_lot)
    ret = sell(price, g.FUTURE_ID, lot_type = " ")
    if ret == None:
        return False

    new_lot = query_lot()
    print 'new lot = ' + str(new_lot)
    if new_lot < (old_lot + 1):
        return False
    else:
        return True

def withdraw_or_not(price):
    # TODO
    return False

def withdraw(price):
    old_lot = query_lot()
    if old_lot < 0:
        ret = buy(price)
        return ret
    elif old_lot > 0:
        ret = sell(price)
        return ret
    else:
        print "You have nothing to offset, Mr. Loser."
    return False

def print_status():
    print("# -- " + str(datetime.now()) + " -- #")
    print "Remaining g.lot(s) = ", g.lot
    if g.lot > 0:
        print "buy_list = " + str(g.buy_list)
    elif g.lot < 0:
        print "sell_list = " + str(g.sell_list)
    print
