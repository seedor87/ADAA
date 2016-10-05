
from __future__ import division
import sys, timeit
from random import randint
from functools import wraps
import random

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = timeit.default_timer()
        result = function(*args, **kwargs)
        t1 = timeit.default_timer()
        diff = t1 -t0
        return result, function.func_name, diff
    return func_timer

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def randomize_in_place(List):
    for i in range(0, len(List)-1):
        exchange(List, i, randint(i, len(List)-1))
    return List

@timer
def qsort_selection(List, i):
    """
    This method involves first quick-sorting the list of values then indexing the required output for a solution
    """
    return _qsort(List)[i-1]

def _qsort(List):
    if List == []:
        return []
    else:
        pivot = List[0]
        lesser = _qsort([x for x in List[1:] if x < pivot])
        greater = _qsort([x for x in List[1:] if x >= pivot])
        return lesser + [pivot] + greater

@timer
def partition_selection(List, i, p=None, r=None):
    """
    This method applies the partition investigation to the list to find the location of the i parameter smallest index
    """
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

def partition(List, p, r):
    idx = random.randint(p, r)
    x = List[idx]
    for j in range(p, r):
        if List[j] <= x:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p

"""All Prime Numbers Under 1000"""
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def main():
    input = randomize_in_place(primes)
    print "\nInput: %s\nEnter a choice of ith smallest number, or q to quit--\n" % (input)
    while True:
        try:
            n = raw_input(">> ")
            if n == "q":
                print "exiting"
                break
            else:
                loc = int(n) -2
                if loc < -1 or int(n) > len(input):
                    print '!!! Invalid index !!!'
                else:
                    print 'Value: %s\tRuntime: %s, %s' % (partition_selection(input, loc))
                    print 'Value: %s\tRuntime: %s, %s' % (qsort_selection(input, int(n)))
        except Exception as e:
            pass

main()
sys.exit(0)