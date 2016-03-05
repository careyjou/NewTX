from T4 import buy_api, sell_api
import sys, time

lot = 0
lot_limit = 1
k_day = 0
k_60 = 0

def print_remaining_lot():
    print "Remaining lot(s) = ", lot

def update_k_60():
    pass

def update_k_day():
    pass

def is_up_trend(price):
    return True

def is_down_trend(price):
    return True

def buy(price):
    global lot
    if buy_api() == True:
        lot +=1
        print_remaining_lot()

def sell(price):
    global lot
    if sell_api() == True:
        lot -=1
        print_remaining_lot()

def withdraw_or_not(price):
    return True

def withdraw(price):
    global lot
    if lot < 0:
        lot +=1
        print_remaining_lot()
    elif lot > 0:
        lot -=1
        print_remaining_lot()

def monitor_loop():
    global lot
    global lot_limit

    try:
        while True:
            update_k_day()
            update_k_60()
            if abs(lot) < lot_limit:
                if is_up_trend(k_day) and is_up_trend(k_60):
                    buy(k_60)
                elif is_down_trend(k_day) and is_down_trend(k_60):
                    sell(k_60)

            elif abs(lot) > 0:
                if withdraw_or_not(k_60):
                    withdraw(k_60)
    except KeyboardInterrupt:
        print "Interrupted."

monitor_loop()
