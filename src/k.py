''' all operations related to k bar is put here '''
import os
import mtx
import json
from datetime import datetime, timedelta

time_price = dict()
yesterday_time_price = dict()
legal_hour = map(str,range(8,14))

# TODO: FOR TESTING
TEST_PRICE = 8500

def update_k_60():
    curr_time = strftime("%H%M")
    curr_date = strftime("%Y%m%d")
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

    with open(infile, 'r') as infile:
        yesterday_time_price = json.loads(infile.read())
    return yesterday_time_price

def k_day_trend():
    # TODO
    return 1

def k_60_trend():
    # TODO
    return 1

if __name__ == '__main__':
    print update_k_day()
