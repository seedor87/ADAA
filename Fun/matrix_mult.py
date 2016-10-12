from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps
import matplotlib.pyplot as plt
from pprint import pprint

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' %(highlight, text, color.END)

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
def recursive_matrix_chain(p):
    return _recursive_matrix_chain(p, 0, len(p) - 1)

def _recursive_matrix_chain(p,i,j):

    if i==j:
        return 0
    q = sys.maxint
    for k in range(i,j):
        q = min(q, _recursive_matrix_chain(p,i,k)+
                _recursive_matrix_chain(p,k+1,j)+
                (p[i-1]*p[k]*p[j]))
    return q

@timer
def memoized_matrix_chain(p):
    n = len(p)
    temp = xrange(0, n)
    m = [[0 for _ in temp] for _ in temp]

    # m = [None] * (n+1)
    # for i in range(0, n + 1):
    #     m[i] = []
    #     for j in range(0, n + 1):
    #         m[i].append(0)

    for i in range(0, n):
        for j in range(i, n):
            m[i][j] = sys.maxint
    return _lookup_chain(m, p, 0, n-1)

def _lookup_chain(m, p, i, j):
    if m[i][j] < sys.maxint:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = _lookup_chain(m, p, i, k)+_lookup_chain(m, p, k+1, j)+(p[i-1]*p[k]*p[j])
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

array = [2, 4, 6, 3, 4, 7]
print recursive_matrix_chain(array)[0]
print memoized_matrix_chain(array)[0]

array = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print recursive_matrix_chain(array)[0]
print memoized_matrix_chain(array)[0]

array = [56, 43, 57, 97, 99, 8, 1, 50, 79, 16, 89, 51, 20, 87, 11, 90]
print recursive_matrix_chain(array)[0]
print memoized_matrix_chain(array)[0]