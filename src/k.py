''' all operations related to k bar is put here '''
import os
import mtx
import json
from datetime import datetime, timedelta
import time
import firebase

time_price = dict()
yesterday_time_price = dict()
legal_hour = map(str,range(8,14))

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

def update_k_day1():
	date_delta=1
	MONDAY, SUNDAY=0 ,6

	MYURL  = 'https://boiling-heat-5294.firebaseio.com/'
	EMAIL  = 'emersonhtc@gmail.com'
	SECRET = '5zF8T37NlZB1HBHkb9T1zAZ6c2cPbXiXlzP5yJ8P'

	authentication = firebase.FirebaseAuthentication(SECRET,EMAIL, True, True)
	fb = firebase.FirebaseApplication(MYURL, authentication)

	today = datetime.now().date()
	date_delta = 3 if today.weekday() == MONDAY else 1
	date_delta = 2 if today.weekday() == SUNDAY else 1

	last_trade_date = today - timedelta(date_delta)
	access_str = str(last_trade_date).replace('-','/')
	return fb.get(access_str,None)

def k_day_trend():
	# TODO
	return 1

def k_60_trend():
	# TODO
	return 1

if __name__ == '__main__':
	print update_k_day1()
