from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps
import matplotlib.pyplot as plt

rand_list_rand_len = lambda Len=100, Elems=['A', 'B', 'C', 'D']: [Elems[randint(1, len(Elems)-1)] for _ in range(randint(1,Len))]

def randomize_in_place(List):

    def exchange(List, a, b):
        temp = List[a]
        List[a] = List[b]
        List[b] = temp

    for i in range(0, len(List)-1):
        exchange(List, i, randint(i, len(List)-1))
    return List

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
def longest_common_subsequence_recursion(xstr, ystr):
    return _longest_common_subsequence_recursion(xstr, ystr)

def _longest_common_subsequence_recursion(xstr, ystr):
    """
    >>> longest_common_subsequence_recursion('thisisatest', 'testing123testing')[0]
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + _longest_common_subsequence_recursion(xs, ys)
    else:
        return max(_longest_common_subsequence_recursion(xstr, ys), _longest_common_subsequence_recursion(xs, ystr), key=len)


@timer
def longest_common_subsequence_dynamic(a, b):
    return _longest_common_subsequence_dynamic(a, b)

def _longest_common_subsequence_dynamic(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result


if __name__ == '__main__':

    import doctest

    doctest.testmod()

    Elems = 'abcdefghijklmenopqrstuvwxyz'
    input1 = rand_list_rand_len(Len=15, Elems=Elems)
    input2 = rand_list_rand_len(Len=15, Elems=Elems)

    print input1
    print input2

    print longest_common_subsequence_recursion(input1, input2)
    print longest_common_subsequence_dynamic(input1, input2)


