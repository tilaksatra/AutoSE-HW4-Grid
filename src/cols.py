import re
from num import Num
from sym import Sym

class Col:
    '''
    Create Num or Sym for non-slipped columns Columns 
    '''
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for n,s in enumerate(t):
            if re.search(r'^[A-Z]', s) :
                col=Num(s,n)
            else:
                col=Sym(s,n)
            self.all.append(col)

            if not s[-1]=='X': 
                if "!" in s:
                    self.klass=col                           
                isY = re.search(r'[!+-]', s)
                if isY:
                    self.y.append(col)
                else:
                    self.x.append(col)
                
    def add(self, row):
        '''
        Add row to columns
        '''
        for list in [self.x, self.y]:
            for col in list:
                col.add(row.cells[col.at])

