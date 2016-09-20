from __future__ import division
import sys, timeit
from random import randint, uniform
from functools import wraps

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

def quickSort(List, p=0, r=None):
    if r is None:
        r = len(List)-1
    if p < r:

       q = partition(List, p, r)
       quickSort(List, p, q-1)
       quickSort(List, q+1, r)
    return List


def partition(List, p, r):
    x = List[p]
    i = p
    for j in range(p+1, r):
        if List[j] <= x:
            exchange(List, j, i)
    exchange(List, p+1, r)
    return i

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp


# input = list_rand_int(10,20,Sign=-1)
input = [-40, 50, 0, 10, 20, -25, 5, 0]
res = quickSort(input)
print(res)