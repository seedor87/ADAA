from __future__ import division
import sys, timeit
from random import randint
from functools import wraps
import matplotlib.pyplot as plt

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


def scatter_style(*y_args):
    colors = ['red', 'green', 'blue']
    index_for_keys = 0
    table_for_keys = []
    for y_set in y_args:
        x_val = 1
        color = colors[index_for_keys]
        for result in y_set:
            plt.scatter(x_val, result, color=color)
            x_val += 1
        table_for_keys.append((plt.Rectangle((0, 0), 0.1, 0.1, fc=color), 'line arg_' + str(index_for_keys)))
        index_for_keys += 1

    plt.legend(*zip(*table_for_keys), loc='upper left')

    return plt


def lines_style(*y_args):
    colors = ['red', 'green', 'blue']
    index_for_keys = 0
    table_for_keys = []
    i_set = [i for i in xrange(1, len(y_args[0]) + 1)]
    for y_set in y_args:
        color = colors[index_for_keys]
        plt.plot(i_set, y_set, color=color)
        table_for_keys.append((plt.Rectangle((0, 0), 0.1, 0.1, fc=color), 'line arg_' + str(index_for_keys)))
        index_for_keys += 1

    plt.legend(*zip(*table_for_keys), loc='upper left')

    return plt


if __name__ == '__main__':
    test_set = [[2, 4, 6, 3, 4, 7],
                [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
                [56, 43, 57, 97, 99, 8, 1, 50, 79, 16, 89, 51, 20, 87, 90]]

    # test_set = [list_rand_int(100, x, 0) for x in xrange(2,20)]
    # test_set = [[1],
    #             [37, 74],
    #             [10, 65, 72],
    #             [54, 100, 38, 84],
    #             [58, 66, 6, 5, 24],
    #             [69, 17, 35, 15, 73, 74],
    #             [17, 66, 75, 20, 29, 50, 56],
    #             [68, 36, 59, 9, 36, 96, 33, 9],
    #             [48, 93, 17, 37, 52, 64, 58, 26, 99],
    #             [60, 69, 9, 31, 65, 53, 12, 17, 69, 49],
    #             [61, 42, 10, 49, 31, 16, 3, 12, 31, 38, 61],
    #             [96, 14, 70, 61, 35, 17, 24, 8, 91, 46, 81, 78],
    #             [97, 59, 35, 98, 25, 37, 77, 58, 8, 5, 78, 44, 35],
    #             [38, 41, 78, 48, 50, 78, 34, 21, 70, 3, 79, 33, 15, 31],
    #             [28, 85, 3, 47, 0, 13, 58, 16, 74, 86, 76, 64, 92, 97, 27],
    #             [59, 25, 2, 11, 9, 92, 2, 50, 32, 86, 24, 37, 28, 74, 56, 48]]  # approx 9 seconds
    #             # [67, 42, 92, 58, 72, 61, 17, 12, 67, 58, 24, 45, 71, 21, 34, 14, 64],
    #             # [15, 91, 42, 67, 24, 11, 81, 54, 42, 25, 55, 93, 87, 13, 34, 26, 43, 98],
    #             # [53, 34, 3, 86, 61, 20, 2, 76, 12, 1, 29, 95, 93, 22, 56, 66, 44, 6, 14]]

    y1 = []
    y2 = []
    for test in test_set:
        res1 = recursive_matrix_chain(test)[1]
        res2 = memoized_matrix_chain(test)[1]
        y1.append(res1)
        y2.append(res2)

    plt = scatter_style(y1, y2)

    plt.xlabel('This is my x-axis')
    plt.ylabel('This is your y-axis')
    plt.title("This is our title")

    plt.grid()
    plt.show()


    plt = lines_style(y1, y2)

    plt.xlabel('This is my x-axis')
    plt.ylabel('This is your y-axis')
    plt.title("This is our title")

    plt.grid()
    plt.show()