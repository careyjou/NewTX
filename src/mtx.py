import urllib2
import re
import time
import datetime
import BeautifulSoup
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty

Builder.load_file("MtxWidget.kv")

class MtxWidget(Widget):
	price = StringProperty()
	deal_price_ascii = [166,168,165,230,187,249]
	deal_price_str = ""

	TX_url  = "https://www.capitalfutures.com.tw/quotations/default.asp?xy=1&xt=2&StockCode=MTX00"
	TX_start_trade=datetime.time(8,45)
	TX_end_trade=datetime.time(13,45)

	EFTX_url = "http://www.eurexchange.com/exchange-en/products/idx/tai/Daily-Futures-on-TAIEX-Futures/929882"
	EFTX_start_trade=datetime.time(14,45)
	EFTX_end_trade=datetime.time(23,59)

	def __init__(self, **kwargs):
		super(MtxWidget, self).__init__(**kwargs)

	def get_price_TX(self):
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

	def get_price_TX_1(self):
		info = []
		page = urllib2.urlopen(self.TX_url).read()
		soup = BeautifulSoup.BeautifulSOAP(page)
		table = soup.find("table",{ "class" : "type-01" })
		for row in table.findAll("td"):
			for item in row:
				if isinstance(item, BeautifulSoup.NavigableString):	info.append(item)
				if isinstance(item, BeautifulSoup.Tag):	info.append(item.getText())

		info = re.findall(r'([0-9]+\.[0-9]*)', str(info))
		print info[5]
		return info[5]

	def get_price_EFTX_1(self):
		info = []
		req = urllib2.Request(self.EFTX_url, headers={'User-Agent' : "Magic Browser"})
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

	def update(self,dt):
		time = datetime.datetime.now()
		time_str = time.strftime("Time: %H:%M:%S")
		if self.TX_start_trade < time.time() < self.TX_end_trade:
			self.price = str(self.get_price_TX_1()) + "@" + time_str
		else:
			self.price = str(self.get_price_EFTX_1()) + "@" + time_str


	# Tk
	# def clock():
	# 	time = datetime.datetime.now()
	# 	time_str = time.strftime("Time: %H:%M:%S")
	# 	if TX_start_trade < time.time() < TX_end_trade:
	# 		lab['text'] = str(get_price_TX_1()) + "@" + time_str
	# 		root.after(500, clock) # run itself again after 500 ms
	# 	else:
	# 		lab['text'] = str(get_price_EFTX_1()) + "@" + time_str
	# 		root.after(5000, clock) # run itself again after 5000 ms


class MtxApp(App):
    def build(self):
        mtx = MtxWidget()
        Clock.schedule_interval(mtx.update, 5)
        return mtx


if __name__ == '__main__':
	# unit test for getting real time price from capital futures
	# kivy
	MtxApp().run()


	# Tk
	# root = Tk()
	# root.wm_title("TX Monitor")
	# lab = Label(root)
	# lab.pack()
	#
	# # run first time
	# clock()
	#
	# root.mainloop()
