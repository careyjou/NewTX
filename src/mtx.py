import urllib2
import re
import time
import datetime
from Tkinter import *
import BeautifulSoup

deal_price_ascii = [166,168,165,230,187,249]
deal_price_str = ""

url = "https://www.capitalfutures.com.tw/quotations/default.asp?xy=1&xt=2&StockCode=MTX00"

def get_price():
    global deal_price_str
    if deal_price_str == "":
        for i in deal_price_ascii:
            deal_price_str += chr(i)

    resp = urllib2.urlopen(url)
    content = resp.read()
    start = content.find(deal_price_str)
    content = content[start:start+150]
    price = re.findall(r'([0-9]+\.[0-9]*)', content)
    print price[0]
    return price[0]

def get_price_1():
    info = []
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSOAP(page)
    table = soup.find("table",{ "class" : "type-01" })
    for row in table.findAll("td"):
        for item in row:
            if isinstance(item, BeautifulSoup.NavigableString):    info.append(item)
            if isinstance(item, BeautifulSoup.Tag):    info.append(item.getText())

    info = re.findall(r'([0-9]+\.[0-9]*)', str(info))
    return info[5]

if __name__ == '__main__':
    # unit test for getting real time price from capital futures
    root = Tk()
    root.wm_title("MTX Monitor")
    lab = Label(root)
    lab.pack()

    def clock():
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        lab['text'] = str(get_price_1()) + "@" + time
        root.after(500, clock) # run itself again after 500 ms

    # run first time
    clock()

    root.mainloop()
