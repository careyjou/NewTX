import urllib2, BeautifulSoup
import re, time, os, datetime, argparse
from Tkinter import *

deal_price_ascii = [166,168,165,230,187,249]
deal_price_str = ""

TX_url  = "https://www.capitalfutures.com.tw/quotations/default.asp?xy=1&xt=2&StockCode=MTX00"
TX_start_trade=datetime.time(8,45)
TX_end_trade=datetime.time(13,45)

EFTX_url = "http://www.eurexchange.com/exchange-en/products/idx/tai/Daily-Futures-on-TAIEX-Futures/929882"
EFTX_start_trade=datetime.time(14,45)
EFTX_end_trade=datetime.time(23,59)

def get_price_TX():
	# front-end wrapper
	ret = get_price_TX_1()
	if ret.isdigit() == False:
		ret = float(ret.replace(",",""))
	return ret

def get_price_TX_1():
	info = []
	page = urllib2.urlopen(TX_url).read()
	soup = BeautifulSoup.BeautifulSOAP(page)
	table = soup.find("table",{ "class" : "type-01" })
	for row in table.findAll("td"):
		for item in row:
			if isinstance(item, BeautifulSoup.NavigableString):	info.append(item)
			if isinstance(item, BeautifulSoup.Tag):	info.append(item.getText())

	info = re.findall(r'([0-9]+\.[0-9]*)', str(info))
	print info[2]
	return info[2]

def get_price_TX_2():
	global deal_price_str
	if deal_price_str == "":
		for i in deal_price_ascii:
			deal_price_str += chr(i)

	resp = urllib2.urlopen(TX_url)
	content = resp.read()
	start = content.find(deal_price_str)
	content = content[start:start+150]
	price = re.findall(r'([0-9]+\.[0-9]*)', content)
	print price[0]
	return price[0]

def get_price_EFTX():
	# front-end wrapper
	ret = get_price_EFTX_1()
	if ret.isdigit() == False:
		ret = float(ret.replace(",",""))
	return ret

def get_price_EFTX_1():
	info = []
	req = urllib2.Request(EFTX_url, headers={'User-Agent' : "Magic Browser"})
	page = urllib2.urlopen(req).read()
	soup = BeautifulSoup.BeautifulSOAP(page)
	table = soup.find("table")
	for row in table.findAll("td"):
		for item in row:
			for item_i in item:
				if isinstance(item, BeautifulSoup.NavigableString):    info.append(item)
				if isinstance(item, BeautifulSoup.Tag):    info.append(item.getText())

	info = re.findall(r'([0-9,]+\.[0-9]*)', str(info))
	print info[4]
	return info[4]

def clock():
	time_obj = datetime.datetime.now()
	time_str = time_obj.strftime("Time: %H:%M:%S")
	print time_str
	retry = 10
	while retry > 0:
		try:
			if TX_start_trade < time_obj.time() < TX_end_trade:
				lab['text'] = str(get_price_TX()) + "@" + time_str
				root.after(500, clock) # run itself again after 500 ms
				return True
			else:
				lab['text'] = str(get_price_EFTX()) + "@" + time_str
				root.after(5000, clock) # run itself again after 5000 ms
				return True
		except:
			retry -=1
			print "get price fails. I'll try it 5 secs later."
			print "Remaining trial(s) = " + str(retry)
			time.sleep(5)

	return False


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--tk', help='NOT generate a TK window',required=0,action='store_true')
	args = parser.parse_args()
	sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

	if not args.tk:
		root = Tk()
		root.wm_title("TX Monitor")
		lab = Label(root)
		lab.pack()

		# run first time
		clock()

		root.mainloop()
	else:
		while(True):
			time_obj = datetime.datetime.now()
			time_str = time_obj.strftime("%H:%M:%S")
			print time_str,
			if TX_start_trade < time_obj.time() < TX_end_trade:
				get_price_TX()
			else:
				get_price_EFTX()
			time.sleep(30)
