import copy
import math
from utils import *
from rows import Row
from cols import Col
from constants import options


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

    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        c = cols or self.cols.x

        for col in c:
            n += 1
            d += col.dist(row1.cells[col.at], row2.cells[col.at]) ** options['p']

        return (d / n) ** (1 / options['p'])

    def around(self, row1, rows=None, cols=None):

        if rows is None: rows = self.rows

        def function(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        mapped = map(function, rows)
        return sorted(mapped, key=lambda x: x["dist"])

    def better(self, row1, row2):
        s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 -= math.exp(col.w * (x - y) / len(ys))
            s2 -= math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def half(self, rows=None, cols=None, above=None):
        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            return {"row": row, "dist": cosine(dist(row, A), dist(row, B), c)}

        if rows is None: rows = self.rows
        some = many(rows, options['Sample'])
        A = above or any(some)
        B = self.around(A, some)[int(options['Far'] * len(rows))]['row']
        c = dist(A, B)
        left, right, mid = [], [], None
        for n, tmp in enumerate(sorted(list(map(project, rows)), key=lambda x: x["dist"])):
            if n <= len(rows) / 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    def cluster(self, rows=None, min=None, cols=None, above=None):
        if rows is None: rows = self.rows
        min = min or len(rows) ** options['min']
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            node['left'] = self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])

        return node

    def furthest(self, row1, rows=None, cols=None):
        t = self.around(row1, rows, cols)
        furthest = t[len(t) - 1]
        return furthest

    def sway(self, rows=None, min=None, cols=None, above=None):
        if rows == None: rows = self.rows
        min = min or len(rows) ** options['min']
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            if self.better(node['B'], node['A']):
                left, right, node['A'], node['B'] = right, left, node['B'], node['A']
            node['left'] = self.sway(left, min, cols, node['A'])
        return node