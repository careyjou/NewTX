from T4 import buy_api, sell_api
from datetime import datetime
import sys, time, os

lot = 0
lot_limit = 1
buy_list = []
sell_list = []

# TODO: FOR TESTING
TEST_PRICE = 8500

def print_status():
    print("# -- " + str(datetime.now()) + " -- #")
    print "Remaining lot(s) = ", lot
    if lot > 0:
        print buy_list
    elif lot < 0:
        print sell_list
    print

def update_k_60():
    return TEST_PRICE

def update_k_day():
    return TEST_PRICE

def k_day_trend():
    return 1

def k_60_trend():
    return 1

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
