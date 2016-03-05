

if K_Day is up:
    if empty():
        if buy_or_not(K_60):
            buy(K_60)
    else:
        if withdraw_or_not(K_60):
            withdraw(K_60)

elif K_Day is down:
    if empty():
        if sell_or_not(K_60):
            sell(K_60)
    else:
        if withdraw_or_not(K_60):
            withdraw(K_60)
