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
        return '%s%s%s' % (highlight, text, color.END)

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
def memoized_cut_rod(p, n):
    memoize = {1:p[0]}
    return _memoized_cut_rod(p, n, memoize)

def _memoized_cut_rod(p, n, memoize):
    max_val = 0
    for i in range(1, n+1):
        if memoize.get(n-1) is not None:
            cur_max = memoize.get(n-1)
        else:
            cur_max, memoize = _memoized_cut_rod(p, n-1, memoize)
        max_val = max(max_val, p[i-1] + cur_max)
    memoize[n] = max_val
    return max_val, memoize

@timer
def bottom_up_cut_rod(p, n):
    r = s = [0] * (n+1)
    r[0] = 0

    for i in range(1, n + 1):
        max_val = -maxint
        for j in range(i):
            if max_val < p[j] + r[i-j-1]:
                max_val = p[j] + r[i-j-1]
                s[i] = j
        r[i] = max_val

    temp = n
    ret = []
    while temp > 0:
        ret.append(s[temp])
        temp = temp - s[temp]
    return r[n], ret

p = [1,2,3,5,7,9,13,15,16,18,25,30,35,50,60,80,120,150,190,210,220,225,230,230,215,215,210]
for i in range(1, len(p)):
    print 'n = %s' % (wrap_text(str(i), color.RED))
    print '\tsolution: %s, runtime: %s' % tuple([wrap_text(text, color.GREEN) for text in naive_cut_rod(p, i)])
    print '\tsolution: %s, runtime: %s' % tuple([wrap_text(text, color.GREEN) for text in memoized_cut_rod(p, i)])
    print '\tsolution: %s, runtime: %s' % tuple([wrap_text(text, color.GREEN) for text in bottom_up_cut_rod(p, i)])
    print '-' * 100
