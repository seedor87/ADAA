from functools import wraps
from sys import maxint
import sys, timeit


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' %(highlight, text, color.END)

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = timeit.default_timer()
        result = function(*args, **kwargs)
        t1 = timeit.default_timer()
        diff = t1 -t0
        print ("Total time running %s: %s seconds" %(wrap_text(function.func_name, color.DARKCYAN), wrap_text(diff, color.YELLOW)))
        return result, diff
    return func_timer

@timer
def naive_cut_rod(p, n):
    return _naive_cut_rod(p,n)

def _naive_cut_rod(p, n):
    if n == 0:
        return 0
    q = -maxint
    for i in range(0, n+1):
        q = max(q, p[i] + _naive_cut_rod(p, n-i-1))
    return q

@timer
def better_cut_rod(p, n):
    val = [0 for _ in range(n+1)]
    val[0] = 0

    for i in range(1, n+1):
        max_val = -maxint
        for j in range(i):
             max_val = max(max_val, p[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]


stopping_pt = 13
p = [1,2,3,5,7,9,13,15,16,18,25,30,35]
for i in range(1, stopping_pt):
    print naive_cut_rod(p, i)

print """Break""" + '-' * 100
for i in range(1, stopping_pt):
    print better_cut_rod(p, i)