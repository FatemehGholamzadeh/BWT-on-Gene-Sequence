from builtins import range, len, sorted

import numpy as np

from docIO import write_l, read_l


class BWT:
    def __init__(self, dna):
        self.c = {}
        # self.l = self.get_l(self.make_table(dna))
        self.l = [character for character in read_l()]
        self.unq = self.unique(self.l)
        self.get_c()

    def unique(self, list1):
        x = np.array(list1)
        return np.unique(x)

    def make_table(self, dna):
        fl = []
        dna = dna + "$"
        fl.append([dna[0], dna[-1]])
        print("???")
        print(len(dna) - 1)
        for i in range(len(dna) - 1):
            print(str(i) + "  " + str(fl[i]))
            dna = dna[1:] + dna[0:1]
            fl.append([dna[0], dna[-1]])
        print("OOOOOOOOOOOOOOOOOOOO")
        fl = sorted(fl, key=lambda x: x[0])
        return fl

    def get_l(self, table):
        l = [sub[-1] for sub in table]
        write_l(l)
        return l

    def get_c(self):
        self.c["$"] = 0
        fst = sorted(self.l)
        for i in range(len(self.unq)):
            self.c[self.unq[i]] = fst.index(self.unq[i])

    def get_occ(self, c, p):
        return self.l[1:p].count(c)

    def backward_search(self, read):
        i = len(read)
        c = read[-1]
        first = self.c[c] + 1
        next = self.get_next(c)
        if next is None:
            last = len(self.l)-1
        else :
            last = self.c[next]
        while first <= last and i >= 2:
            c = read[i - 2]
            first = self.c[c] + self.get_occ(c, first - 1) + 1
            last = self.c[c] + self.get_occ(c, last)
            i -= 1
        if last < first:
            return None
        else:
            return {"First": first, "Last": last, "number of repeats": last - first + 1}

    def get_next(self, c):
        index = np.where(self.unq == c)[0][0]
        if len(self.unq) - 1 < index + 1:
            return None
        return self.unq[index + 1]

# bwt = BWT("mississipi")
# print(bwt.backward_search("ssi"))
