''' all operations related to k bar is put here '''
import os
import mtx
import json
from datetime import datetime, timedelta
import time
import FirebaseUtil
import g
import calendar
from Ellie_Util.utils import get_Nday_price

time_price = dict()
legal_hour = map(str,range(8,14))
fb = FirebaseUtil.FirebaseUtil()

# TODO: FOR TESTING
TEST_PRICE = 8500

def update_k_60():
    curr_hour = time.strftime("%H")
    curr_min = time.strftime("%M")
    curr_date = time.strftime("/%Y/%m/%d/")
    curr_time = curr_hour + curr_min
    # update
    if curr_min == "45" and curr_hour in legal_hour:
        price = mtx.get_price()
        # 0945 = 09 + 45
        time_price[curr_time] = price
        key = curr_date + curr_time
        instance.put(key, price)

        # update the internal data structure
        # TODO: What if we start this program in the middle of the business hour?
        time_price = json.loads(fb.get(curr_date))

        if int(curr_min) >= 45:
            return time_price[curr_hour + "45"]
        elif int(curr_min) <= 44:
            last_60_k_time = str(int(curr_hour)-1) + "45"
            return time_price[last_60_k_time]
        else:
            raise Exception("This is impossible...")

def today():
    return datetime.now().date()

def k_day_trend():
    prices = get_Nday_price('MTX', 5)[0:-1]
    print prices
    last_4_avg = sum(prices)/len(prices)
    print last_4_avg

    # Derivation:
    # (x1+x2+x3+x4+now)/5 >= (x1+x2+x3+x4)/4 + UP_THRESHOLD
    # 4now >= x1 + x2 + x3 + x4 + 20UP_THRESHOLD
    # now >= last_4_avg + 5UP_THRESHOLD
    curr_price = mtx.get_price_TX()
    if curr_price >= (last_4_avg + 5*g.UP_THRESHOLD):
        return 1
    elif curr_price <= (last_4_avg - 5*g.BOTTOM_THRESHOLD):
        return -1
    else:
        return 0

def k_60_trend():
    # TODO
    return 1

if __name__ == '__main__':
    print k_day_trend()
