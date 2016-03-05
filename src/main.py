from T4 import *
from datetime import datetime
from k import *
import sys, time, os

lot = 0
lot_limit = 1
buy_list = []
sell_list = []

def print_status():
    print("# -- " + str(datetime.now()) + " -- #")
    print "Remaining lot(s) = ", lot
    if lot > 0:
        print buy_list
    elif lot < 0:
        print sell_list
    print

def buy(price):
    global lot
    if buy_api() == True:
        lot +=1
        buy_list.append(price)

def sell(price):
    global lot
    if sell_api() == True:
        lot -=1
        sell_list.append(price)

def withdraw_or_not(price):
    return False

def withdraw(price):
    global lot
    if lot < 0:
        lot +=1
    elif lot > 0:
        lot -=1

def monitor_loop():
    global lot
    global lot_limit

    try:
        while True:
            k_day = update_k_day()
            k_60 = update_k_60()

            if abs(lot) > 0 and withdraw_or_not(k_60):
                withdraw(k_60)
            elif abs(lot) < lot_limit:
                if k_day_trend() == 1 and k_60_trend() == 1:
                    buy(k_60)
                elif k_day_trend() == -1 and k_60_trend() == -1:
                    sell(k_60)
            else:
                print_status()
                time.sleep(1)

    except KeyboardInterrupt:
        print "Interrupted."

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
monitor_loop()
