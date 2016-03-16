''' all operations related to k bar is put here '''
from time import strftime
import mtx

time_price = dict()

# TODO: FOR TESTING
TEST_PRICE = 8500

def update_k_60():
    curr_time = strftime("%Y%m%d%H%M")
    if curr_time.endswith("45"):
        time_price[curr_time] = mtx.get_price()

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
