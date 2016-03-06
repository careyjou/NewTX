import urllib2
import re

deal_price_ascii = [166,168,165,230,187,249]
deal_price_str = ""

def get_price():
    global deal_price_str
    if deal_price_str == "":
        for i in deal_price_ascii:
            deal_price_str += chr(i)

    url = "https://www.capitalfutures.com.tw/quotations/default.asp?xy=1&xt=2&StockCode=MTX00"
    resp = urllib2.urlopen(url)
    content = resp.read()
    start = content.find(deal_price_str)
    content = content[start:start+150]
    price = re.findall(r'([0-9]+\.[0-9]*)', content)
    print price[0]
    return price[0]

if __name__ == '__main__':
    # unit test for getting real time price from capital futures
    get_price()
