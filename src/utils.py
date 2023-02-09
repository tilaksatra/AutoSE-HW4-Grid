import math
import re
import sys
import io

sys.path.append("./src")
from constants import *

seed = 937162211

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

# map method 'fun'(v) over list (skip nil results)
def map(t, fun):
    u = {}
    for k,v in enumerate(t):
        o = fun(v)
        v, k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1 + len(u)] = v
    return u

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
    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return  False
        return s1

    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(s)
    except Exception as exception:
        print("Coerce Error", exception)

# Method to print values
def oo(t):
    o(t, False)

# Method to format string values
def o(t, is_keys = True):
    if type(t) is not dict:
        return str(t)
    def fun(k,v):
        if str(k).find('^_') == -1:
            return format(':{} {}', o(k), o(v))

    if len(t) > 0 and not is_keys:
        return '{' + ' '.join(str(content) for content in map(t, o)) + '}'
    else:
        return '{' + ' '.join(str(content) for content in kap(t, fun)) + '}'

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