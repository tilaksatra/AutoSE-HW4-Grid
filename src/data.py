import copy
from utils import kap, csv
from rows import Row
from cols import Col

class DATA:
    def __init__(self, src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            csv(src, self.add)
        else:
            for t in src:
                self.add(t)

    def clone(self, init):
        '''
        Returns clone of data
        '''
        return copy.deepcopy(self)
    
    def add(self, t):
        '''
        Adds row
        '''
        if self.cols:
            if type(t) == list:
                t = Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Col(t)
    

    def stats(self, what, cols, nPlaces):
        def fun(_, col):
            if what == 'mid':
                val = col.mid()
            else:
                val = col.div()
            return col.rnd(val, nPlaces), col.txt
        return kap(cols or self.cols.y, fun)
