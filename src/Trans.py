import json

class Entry:
    BorS = None
    price = None
    id = None

    def __init__(self, BorS, price, id):
        self.BorS = BorS
        self.price = price
        self.id = id

    def __str__(self):
        ret = json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
        return ret

class Trans:
    trans = []
    index = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            result = self.trans[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def addTran(self, t):
        self.trans.append(t)

    def delTran(self, t):
        self.trans.remove(t)

    def __str__(self):
            ret = json.dumps(self.trans, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ret = "{" + ret[1:-1] + "}"
            return ret

    def __len__(self):
        return len(self.trans)

if __name__ == '__main__':
    trans_summary = Trans()
    entry = Entry("B", 8700, "vn888")

    print "add entry"
    trans_summary.addTran(entry)
    # print len(trans_summary)
    # print trans_summary
    for tran in trans_summary:
        print tran

    print "del entry"
    trans_summary.delTran(entry)
    print trans_summary
