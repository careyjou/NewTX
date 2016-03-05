lot = 0
lot_Limit = 1

def buy(price):
    if buy_api() == True:
        lot +=1

def sell(price):
    if sell_api() == True:
        lot +=1

def monitor_loop():
    global lot
    global lot_limit

    while True:
        if lot < lot_limit:
            if is_up_trend(K_Day) and is_up_trend(K_60):
                buy(K_60)
            elif is_down_trend(K_Day) and is_down_trend(K_60)
                sell(K_60)

        elif lot > 0:
            if withdraw_or_not(K_60):
                withdraw(K_60)

        ch = 0xFF & cv2.waitKey(5)
        if ch == 27:
            break

monitor_loop()
