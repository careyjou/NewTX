import json

class Tran:
    B_or_S, price, id = None, None, None

    def __init__(self, B_or_S, price, id):
        self.B_or_S, self.price, self.id = B_or_S, price, id

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

    def del_tran(self, id):
        for i in self.trans:
            if i.id == id:
                self.trans.remove(i)
                return True
        return False

    def __str__(self):
            ret = json.dumps(self.trans, default=lambda o: o.__dict__,sort_keys=True, indent=4)
            ret = "{" + ret[1:-1] + "}"
            return ret

    def __len__(self):
        return len(self.trans)

if __name__ == '__main__':
    trans_summary = Trans()
    tran = Tran("B", 8700, "vn888")
    tran2 = Tran("S", 8600, "vn777")
    print "Add trans"
    trans_summary.add_tran(tran)
    trans_summary.add_tran(tran2)
    # print len(trans_summary)
    # print trans_summary
    for tran in trans_summary:
        print tran

    print "Del tran vn888:", trans_summary.del_tran("vn888")
    print trans_summary
