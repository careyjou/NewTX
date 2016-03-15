#!/usr/bin/env python
# -*- coding: UTF-8 -*-
''' the bridge that connects strategy to Sinopac's API '''
from py4j.java_gateway import JavaGateway
import time;

gateway = JavaGateway()
instance = gateway.entry_point.getInstance()

def buy_api(price,amount):
    old_lot = query_lot()
    print 'old lot = ' + str(old_lot)
    ret = instance.buy(price,amount)
    if ret == None:
        return False

    new_lot = query_lot()

    print 'new lot = ' + str(new_lot)
    if new_lot < (old_lot + amount):
        return False
    else:
        return True

def sell_api(price,amount):
    old_lot = query_lot()
    print 'old lot = ' + str(old_lot)
    ret = instance.sell(price,amount)
    if ret == None:
        return False

    new_lot = query_lot()

    print 'new lot = ' + str(new_lot)
    if new_lot < (old_lot + amount):
        return False
    else:
        return True

def query_lot():
    ret = query_unsettled()
    return ret[11]

def query_unsettled():
    ret = instance.queryUnsettled().encode("big5")
    while ret.find('Error') != -1:
        time.sleep(5)
        ret = instance.queryUnsettled().encode("big5")
        
    # TODO: What will be returned if the # of lot = 0?
    list = ret.split()
    return list
