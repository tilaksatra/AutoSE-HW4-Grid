import sys

sys.path.append("./src")

from main import *
from utils import *
from num import *
from sym import *
from data import *

n = 0

def test_the():
    oo(options)
    return True

def test_sym():
    symObj = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        symObj.add(x)
    return "a" == symObj.mid() and 1.379 == rnd(symObj.div(), 3)

def test_num():
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div(), 3)

def test_stats():
    data = DATA(options['file'])
    dataDict = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in dataDict.items():
        print(k, 'mid', data.stats('mid', cols, 2))
        print(' ', 'div', data.stats('div', cols, 2))
        print()
    return True

def test_data():
    dataObj = DATA(options['file'])
    return len(dataObj.rows) == 398 and \
        dataObj.cols.y[0].w == -1 and \
        dataObj.cols.x[1].at == 1 and \
        len(dataObj.cols.x) == 4

def test_optimize():
    data = DATA(options['file'])
    show(data.sway(),'mid',data.cols.y,1)

def test_around():
    data = DATA(options['file'])
    print(0, 0, data.rows[1].cells)
    for n, t in enumerate(data.around(data.rows[1])):
        if n % 50 == 0:
            print(n, rnd(t['dist'], 2), t['row'].cells)

def test_clone():
    data1Obj = DATA(options['file'])
    data2Obj = data1Obj.clone(data1Obj.rows)
    return (data1Obj.cols.x[1].at == data2Obj.cols.x[1].at) and \
        (data1Obj.cols.y[1].w == data2Obj.cols.y[1].w) and \
        (len(data1Obj.cols.x) == len(data2Obj.cols.x)) and \
         (len(data1Obj.rows) == len(data2Obj.rows))

def test_half():
    data = DATA(options['file'])
    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(A.cells, c)
    print(mid.cells)
    print(B.cells)

def test_cluster():
    data = DATA(options['file'])
    show(data.cluster(), "mid", data.cols.y, 1)


if __name__ == '__main__':
    eg('around', 'sorting nearest neighbors', test_around)
    eg('clone', 'duplicate structure', test_clone)
    eg('cluster', 'N-level bi-clustering', test_cluster)
    eg('data', 'read DATA csv', test_data)
    eg('half', '1-level bi-clustering', test_half)
    eg('num', 'check nums', test_num)
    eg('optimize', 'semi-supervised optimization', test_optimize)
    eg('sym', 'check syms', test_sym)
    eg('the', 'show settings', test_the)
    eg('stats', 'stats from DATA', test_stats)
    main(options, help, egs)