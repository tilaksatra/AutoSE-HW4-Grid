import sys

sys.path.append("./src")

from main import *
from utils import *
from num import *
from sym import *
from data import *

n = 0


def test_the():
    # oo(options)
    print(options)
    return True


def test_copy():  # copy
    t1 = {'a': 1, 'b': {'c': 2, 'd': [3]}}
    t2 = utils.copy(t1)
    t2['b']['d'][0] = 10000
    print('b4', t1, '\nafter', t2)


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


def test_repCols():
    t = repCols(dofile(options['file'])['cols'], DATA)
    for col in t.cols.all:
        oo(col)
    for row in t.rows:
        oo(row)


def test_repRows():
    t = dofile(options['file'])
    rows = repRows(t, transpose(t['cols']), DATA)
    for col in rows.cols.all:
        oo(col)
    for row in rows.rows:
        oo(row)


def test_synonyms():
    data = DATA(options['file'])
    show(repCols(dofile(options['file'])['cols'], DATA).cluster())


def test_prototypes():
    t = dofile(options['file'])
    rows = repRows(t, transpose(t['cols']), DATA)
    show(rows.cluster(), "mid", rows.cols.all, 1)


def test_position():
    t = dofile(options['file'])
    rows = repRows(t, transpose(t['cols']), DATA)
    rows.cluster()
    repPlace(rows)


def test_every():
    repgrid(options['file'], DATA)


if __name__ == '__main__':
    eg('the', 'check the', test_the)
    eg('copy', 'check copy', test_copy)
    eg('num', 'check nums', test_num)
    eg('sym', 'check syms', test_sym)
    eg('repcols', 'checking repcols', test_repCols)
    eg('reprows', 'checking reprows', test_repRows)
    eg('synonyms', 'checking repcols cluster', test_synonyms)
    eg('prototypes', 'checking reprows cluster', test_prototypes)
    eg('position', 'where\'s wally', test_position)
    eg('every', 'the whole enchilada', test_every)
    main(options, help, egs)
