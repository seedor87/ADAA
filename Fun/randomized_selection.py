
from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = timeit.default_timer()
        result = function(*args, **kwargs)
        t1 = timeit.default_timer()
        diff = t1 -t0
        return result, diff
    return func_timer

@timer
def partition_selection(List, i, p=None, r=None):
    return _partition_selection(List, p=0, r = len(List)-1, i=i)

def _partition_selection(List, p, r, i):
    if p == r:
        return List[p]
    q = partition(List, p, r)
    k = q-p-1
    if i == k:
        return List[q]
    elif i < k:
        return _partition_selection(List, p, q-1, i)
    else:
        return _partition_selection(List, q+1, r, i-k)

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def partition(List, p, r):
    x = List[r]
    for j in range(p, r):
        if List[j] <= x:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p


input = [3, 5, 7, 9, 11]
print "\nInput: %s\nEnter a choice of ith smallest number, or q to quit--\n" % (input)
while True:
    try:
        n = raw_input(">>" % (input))
        if n == "q":
            print "exiting"
            break
        else:
            loc = int(n) -2
            if loc < -1 or int(n) > len(input):
                print '!!! Invalid index !!!'
            else:
                print 'Value: %s\tRuntime: %s' % (partition_selection(input, loc))
    except Exception as e:
        pass