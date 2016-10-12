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

# test_set = [[2, 4, 6, 3, 4, 7],
#             [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
#             [56, 43, 57, 97, 99, 8, 1, 50, 79, 16, 89, 51, 20, 87, 11, 90]]

# test_set = [list_rand_int(100, x, 0) for x in xrange(2,20)]
test_set = [[1],
           [37, 74],
           [10, 65, 72],
           [54, 100, 38, 84],
           [58, 66, 6, 5, 24],
           [69, 17, 35, 15, 73, 74],
           [17, 66, 75, 20, 29, 50, 56],
           [68, 36, 59, 9, 36, 96, 33, 9],
           [48, 93, 17, 37, 52, 64, 58, 26, 99],
           [60, 69, 9, 31, 65, 53, 12, 17, 69, 49],
           [61, 42, 10, 49, 31, 16, 3, 12, 31, 38, 61],
           [96, 14, 70, 61, 35, 17, 24, 8, 91, 46, 81, 78],
           [97, 59, 35, 98, 25, 37, 77, 58, 8, 5, 78, 44, 35],
           [38, 41, 78, 48, 50, 78, 34, 21, 70, 3, 79, 33, 15, 31],
           [28, 85, 3, 47, 0, 13, 58, 16, 74, 86, 76, 64, 92, 97, 27],
           [59, 25, 2, 11, 9, 92, 2, 50, 32, 86, 24, 37, 28, 74, 56, 48]] # approx 9 seconds
           # [67, 42, 92, 58, 72, 61, 17, 12, 67, 58, 24, 45, 71, 21, 34, 14, 64],
           # [15, 91, 42, 67, 24, 11, 81, 54, 42, 25, 55, 93, 87, 13, 34, 26, 43, 98],
           # [53, 34, 3, 86, 61, 20, 2, 76, 12, 1, 29, 95, 93, 22, 56, 66, 44, 6, 14]]

def scatter_style():
    i = 1
    for test in test_set:
        a = recursive_matrix_chain(test)[1]
        b = memoized_matrix_chain(test)[1]
        plt.scatter(i, a, color='red')
        plt.scatter(i, b, color='green')
        i += 1

    p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc='red')
    p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc='green')

    plt.xlabel('This is my x-axis')
    plt.ylabel('This is your y-axis')
    plt.title("This is our title")

    plt.legend((p1, p2), ('line1', 'line2'), loc='upper left')

    plt.grid()
    plt.show()

def lines_style():
    i = 1
    x = []
    y1 = []
    y2 = []
    for test in test_set:
        a = recursive_matrix_chain(test)[1]
        b = memoized_matrix_chain(test)[1]
        x.append(i)
        y1.append(a)
        y2.append(b)
        i += 1

    plt.plot(x, y1, color='red')
    plt.plot(x, y2, color='green')

    p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc='red')
    p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc='green')

    plt.xlabel('This is my x-axis')
    plt.ylabel('This is your y-axis')
    plt.title("This is our title")

    plt.legend((p1, p2), ('line1', 'line2'), loc='upper left')

    plt.grid()
    plt.show()

if __name__ == '__main__':
    scatter_style()
    lines_style()