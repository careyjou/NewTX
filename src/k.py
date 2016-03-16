''' all operations related to k bar is put here '''
from time import strftime
import mtx
import json

time_price = dict()
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
    # TODO
    return TEST_PRICE

def k_day_trend():
    # TODO
    return 1

def k_60_trend():
    # TODO
    return 1

if __name__ == '__main__':
    update_k_60()
