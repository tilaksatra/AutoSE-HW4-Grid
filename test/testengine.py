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


if __name__ == '__main__':
    eg('num', 'check nums', test_num)
    eg('sym', 'check syms', test_sym)
