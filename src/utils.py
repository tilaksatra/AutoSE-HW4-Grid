import math
import re
import sys
import io
import copy as copyy
import json
from data import DATA

sys.path.append("../src")
from constants import *

seed = 937162211

def repCols(cols):
    cols = copy(cols)
    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    col1=list()
    for i in range(len(cols[1])-1):
        col1 = ['Num' + str(i+1)]
    col1.append('thingX')
    cols.insert(0, col1)
    return DATA(cols)

def repRows(t, rows):
    rows = copy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + str(s)
    rows.pop()
    for n, row in enumerate(rows):
        if (n==0):
            row.append('thingX')
        else:
            u=t["rows"][len(t["rows"])-n]
            row.append(u[len(u) - 1])
    return  DATA(rows)

def repgrid(file):
    t = dofile(file)
    rows = repRows(t, transpose(t['cols']))
    cols = repCols(t['cols'])
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=" "
    maxy = 0
    print("")
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])

        print("===",row.x,row.y)
        print(type(row))
        if( math.isnan(row.x) or math.isnan(row.y)):
            continue
        x=int(row.x*n/1)
        y=int(row.y*n/1)
        maxy = max(maxy, y+1)
        g[y+1][x+1] = c
    print("")
    for y in range(1,maxy+1):
        print(" ".join(g[y].values()))


def dofile(file):
    with open(file, 'r', encoding = 'utf-8') as f:


        text = re.findall(r'(return\s+[^.]+)',  f.read())[0]
        replacements = {'return ' : '', '{' : '[', '}' : ']','=':':', '[\n':'{\n', '\n]':'\n}', '_':'"_"', '\'':'"'}
        for a,b in replacements.items():
            text = text.replace(a, b)
        # print("text1: \n",text1)

        text = re.sub("(\w+):",r'"\1":', text)
        return json.loads(text)


# Util Methods for Numerics
# Random number generator method
def rand(low, high):
    global seed
    if low is None:
        low = 0
    if high is None:
        high = 1
    seed = (16807 * seed) % 2147483647
    return low + (high -low) * seed / 2147483647

# flooring method
def rint(low, high):
    return math.floor(0.5 + rand(low, high))

def rnd(n, n_places):
    if not n_places:
        n_places = 3
    mult = math.pow(10, n_places)
    return math.floor(n * mult + 0.5)/mult

def cosine(a, b, c):
    if c == 0:
        den = 1
    else:
        den = 2*c
    x1 = ((a**2 + c**2 - b**2) / den)
    x2 = max(0, min(x1, 1))
    y = abs((a**2 - x2**2)**0.5)

    return x2, y

def show(node, what = None, cols = None, nPlaces = None, lvl = None):
    if node:
        lvl = lvl or 0
        print("|.." * lvl, str(len(node["data"].rows)), " ")
        if not node.get("left", None) or lvl == 0:
            print(o(node["data"].stats("mid", node["data"].cols.y, nPlaces)))
        else:
            print("")
        show(node.get("left", None), what, cols, nPlaces, lvl + 1)
        show(node.get("right", None), what, cols, nPlaces, lvl + 1)

def many(t, n):
    arr = []
    for index in range(1, n + 1):
        arr.append(any(t))
    return arr

def any(t):
    return t[rint(0, len(t) - 1)]


# map method 'fun'(k,v) over list (skip nil results)
def kap(t, fun):
    u = {}
    for v in t:
        k = t.index(v)
        v, k = fun(k,v)
        u[k or len(u)] = v
    return u

#method that sorts keys
def keys(t):
    return sorted(kap(t, lambda k,x:k))

#method to sort the list
def sort(t, fun):
    return sorted(t, key = fun)

# Util methods for Strings
def coerce(s):
    if s == 'true':
        return True
    elif s == 'false':
        return False
    elif s.isdigit():
        return int(s)
    elif '.' in s and s.replace('.','').isdigit():
        return float(s)
    else:
        return s

def any(t):
    return t[rint(0, len(t) - 1)]

# Method to map values for test cases
def eg(key, str, fun):
    egs[key] = fun
    global help
    help = help + '  -g '+ key + '\t' + str + '\n'

def csv(filename, fun):
    f = io.open(filename)
    while True:
        s = f.readline()
        if s:
            t = []
            for s1 in re.findall("([^,]+)" ,s):
                t.append(coerce(s1))
            fun(t)
        else:
            return f.close()

def copy(t):
    return copyy.deepcopy(t)

def oo(t):
    temp = t.__dict__
    temp['a'] = t.__class__.__name__
    temp['id'] = id(t)
    print(dict(sorted(temp.items())))


import math
import re
import copy as copy_module
import json

seed = 937162211    
# Utility function for numerics
def rint(lo = None, hi = None):
    return math.floor(0.5+rand(lo,hi))

def rand(lo = None, hi = None):
    global seed
    if(lo is None):
        lo=0
    if(hi is None):
        hi=1
    seed=(16807*seed)%2147483647
    return lo+(hi-lo)*seed/2147483647


def rnd(n,nPlaces = None):
    if(nPlaces is None):
        nPlaces=3
    mult=math.pow(10,nPlaces)
    return math.floor(n*mult+0.5)/mult

def cosine(a,b,c):
    '''
    find x,y from a line connecting `a` to `b`
    '''
    c2 = 1 if c == 0 else 2*c
    x1= (a**2+c**2 -b**2)/(c2)
    x2=max(0,min(1,x1))
    y=abs((a**2-x2**2))**0.5
    return x2,y

# Utility functions for lists

# map a function fun(v) over list (skip nil results)
def map( t, fun):
    u = []
    for k,v in enumerate(t):
        o = fun(v)
        v,k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1+len(u)] = v  
    return u


# sort the list with given comparator
def sort( t, fun):
    return sorted(t, key = fun)

# return a function that sorts ascending on 'x'
def lt(x):
    return lambda a,b: a[x]<b[x]

# return sorted list of keys of given list
def keys( t):
    return sort(kap(t,lambda k,_:k))

# returns one items at random
def any(t):
    return t[rint(len(t)-1)]

# return some items from 't'
def many(t,n):
    u=[]
    for i in range(1,n+1):
        u.append(any(t))
    return u

def last(t):
    return t[len(t)-1]

def copy(t):
    return copy_module.deepcopy(t)

# Utility functions for Strings

def o(t, isKeys = None):
    if type(t)!=list:
        return str(t)
    def fun(k,v):
        if str(k).find('^_') == -1:
            return ':{} {}'.format(o(k), o(v))

    if (len(t)>0 and not isKeys):
        return '{' + ' '.join(str(item) for item in map(t,o)) + '}'
    else:
        return '{' + ' '.join(str(item) for item in kap(t,fun)) + '}'

def transpose(t):
    u=[]
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])

    return u

