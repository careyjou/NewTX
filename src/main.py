import T4
from k import *
from g import *
from action import *
import sys, time, os

def monitor_loop():
    try:
        while True:
            k_60 = update_k_60()
            lot = g.lot

            if abs(lot) > 0 and withdraw_or_not(k_60):
                withdraw(k_60)
            elif abs(lot) < lot_limit:
                if k_60_trend() == 1:
                    buy(k_60)
                elif k_60_trend() == -1:
                    sell(k_60)
                else:
                    # TODO: What to do? Cool down?
                    pass
            else:
                print_status()
                time.sleep(5)

    except KeyboardInterrupt:
        print "Interrupted."

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# TODO: For testing
print T4.query_lot()
# T4.buy_api("6000")

monitor_loop()
