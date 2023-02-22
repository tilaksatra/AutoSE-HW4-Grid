import sys

MAX_VALUE = sys.maxsize
MIN_VALUE = -1 * sys.maxsize

help = """
USAGE: testengine.py  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
ACTIONS:
"""


egs = dict()

options =  dict()