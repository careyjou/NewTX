import json

class Entry:
    B_or_S = None
    price = None
    id = None

    def __init__(self, B_or_S, price, id):
        self.B_or_S = B_or_S
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

    def add_tran(self, t):
        self.trans.append(t)

    def del_tran(self, t):
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
    trans_summary.add_tran(entry)
    # print len(trans_summary)
    # print trans_summary
    for tran in trans_summary:
        print tran

    print "del entry"
    trans_summary.del_tran(entry)
    print trans_summary
