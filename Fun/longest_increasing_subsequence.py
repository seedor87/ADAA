from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps
import matplotlib.pyplot as plt


def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' % (highlight, text, color.END)


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
        diff = t1 - t0
        print ("Total time running %s: %s seconds" % (
        wrap_text(function.func_name, color.DARKCYAN), wrap_text(diff, color.YELLOW)))
        return result, diff

    return func_timer

@timer
def longest_increasing_subsequence(p):
    return _longest_increasing_subsequence(p)

def _longest_increasing_subsequence(x):
    n, L = len(x), 0
    P, M = [0] * n, [0] * (n + 1)
    for i in range(n):
        low, high = 1, L
        while low <= high:
            mid = (low + high) // 2
            if (x[M[mid]] < x[i]):
                low = mid + 1
            else:
                high = mid - 1

        new_low = low
        P[i], M[new_low] = M[new_low - 1], i
        if (new_low > L):
            L = new_low
    S, k  = [], M[L]
    for i in range(L-1, -1, -1):
        S.append(x[k])
        k = P[k]
    return S[::-1]

@timer
def longest_increasing_subsequence2(p):
    return _longest_increasing_subsequence2(p)

def _longest_increasing_subsequence2(p):
    n = len(p)
    D = [0] * (n)
    D[0] = 1
    for i in range(1, n):
        D[i] = 1
        for j in range(0, i):
            if p[j] < p[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)


if __name__ == '__main__':
    for d in [[3,2,6,4,5,1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], [18,5,100,3,1,19,6,0,7,4,2]]:
        res, time = longest_increasing_subsequence(d)
        print('a list of increasing sub-sequence of %s is %s in %s seconds' % (wrap_text(d, color.YELLOW), wrap_text(res, color.GREEN), wrap_text(time, color.PURPLE)))
        res, time = longest_increasing_subsequence2(d)
        print('a list of increasing sub-sequence of %s is %s in %s seconds' % (wrap_text(d, color.YELLOW), wrap_text(res, color.GREEN), wrap_text(time, color.PURPLE)))
