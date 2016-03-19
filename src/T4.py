#!/usr/bin/env python
# -*- coding: UTF-8 -*-
''' the bridge that connects strategy to Sinopac's API '''
from py4j.java_gateway import JavaGateway
import time

gateway = JavaGateway()
try:
	instance = gateway.entry_point.getInstance()
except:
	instance = None
	print "T4 unavialable! run at test mode!"

def buy_api(price):
	old_lot = query_lot()
	print 'old lot = ' + str(old_lot)
	ret = instance.buy(price,"1")
	if ret == None:
		return False

	new_lot = query_lot()
	print 'new lot = ' + str(new_lot)
	if new_lot < (old_lot + 1):
		return False
	else:
		return True

def sell_api(price):
	old_lot = query_lot()
	print 'old lot = ' + str(old_lot)
	ret = instance.sell(price,"1")
	if ret == None:
		return False

	new_lot = query_lot()
	print 'new lot = ' + str(new_lot)
	if new_lot < (old_lot + 1):
		return False
	else:
		return True

def query_lot():
	ret = query_unsettled()
	if ret:
		return ret[11]

def query_unsettled():
	if instance:
		ret = instance.queryUnsettled().encode("big5")
		while ret.find('Error') != -1:
			time.sleep(5)
			ret = instance.queryUnsettled().encode("big5")

		if ret.find("MTX") == -1:
			# TODO: What will be returned if the # of lot = 0?
			return 0
		else:
			list = ret.split()
			return list
	else:
		return None