''' all operations related to k bar is put here '''
import os
import mtx
import json
from datetime import datetime, timedelta
import time
import FirebaseUtil

time_price = dict()
yesterday_time_price = dict()
legal_hour = map(str,range(8,14))
fb = FirebaseUtil.FirebaseUtil()

# TODO: FOR TESTING
TEST_PRICE = 8500

def update_k_60():
    curr_time = time.strftime("%H%M")
    curr_date = time.strftime("%Y%m%d")
    if curr_time.endswith("45") and curr_time[0:2] in legal_hour:
        time_price[curr_time] = mtx.get_price()
        outfile = '../history/' + current_date + '.json'
        with open(outfile, 'w') as outfile:
            json.dump(data, outfile)

def update_k_day():
    yesterday_date = datetime.now() - timedelta(1)
    yesterday_str = yesterday_date.strftime("%Y%m%d")
    infile = '../history/' + yesterday_str + '.json'
    while os.path.isfile(infile) != True:
        yesterday_date = yesterday_date - timedelta(1)
        yesterday_str = yesterday_date.strftime("%Y%m%d")
        infile = '../history/' + yesterday_str + '.json'

    print yesterday_date

    with open(infile, 'r') as infile:
        yesterday_time_price = json.loads(infile.read())
    return yesterday_time_price

def last_trade_date(d):
    date_delta = 1
    MONDAY,SUNDAY = 0,6
    date_delta = 3 if d.weekday() == MONDAY else 1
    date_delta = 2 if d.weekday() == SUNDAY else 1
    last = d - timedelta(date_delta)
    return last

def today():
    return datetime.now().date()

def update_k_day1():
    access_str = str(last_trade_date(today())).replace('-','/')
    return fb.get(access_str)

def k_day_trend():
    trade_days = []
    trade_day = today()
    for i in range(1,5):
        trade_day = last_trade_date(trade_day)
        trade_days.append(trade_day)

    trade_days = map(lambda i: str(i).replace('-','/'), trade_days)
    prices = map(lambda i: fb.get(str(i)), trade_days)
    last_4_avg = sum(prices)/len(prices)
    print prices
    print last_4_avg
    # TODO: last 4 prices have been put in prices
    # strategy here
    return 1

def k_60_trend():
    # TODO
    return 1

if __name__ == '__main__':
    k_day_trend()
    print update_k_day1()
    print last_trade_date(today())
