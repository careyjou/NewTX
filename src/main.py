from T4 import *
from datetime import datetime
from k import *
from g import *
from action import *
import sys, time, os

def monitor_loop():
    try:
        while True:
            g.k_day = update_k_day()
            g.k_60 = update_k_60()

            if abs(g.lot) > 0 and withdraw_or_not(g.k_60):
                withdraw(g.k_60)
            elif abs(g.lot) < lot_limit:
                if k_day_trend() == 1 and k_60_trend() == 1:
                    buy(g.k_60)
                elif k_day_trend() == -1 and k_60_trend() == -1:
                    sell(g.k_60)
            else:
                print_status()
                time.sleep(1)

    except KeyboardInterrupt:
        print "Interrupted."

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
monitor_loop()
