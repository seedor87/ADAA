
from __future__ import division
import sys, timeit
from random import randint, uniform
from functools import wraps

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = timeit.default_timer()
        result = function(*args, **kwargs)
        t1 = timeit.default_timer()
        diff = t1 -t0
        print ("Total time running %s: %s seconds" %(function.func_name, diff))
        return result, diff
    return func_timer

@timer
def countingSort(array, start=0, k=100):

    count = [0] * (k+1)

    for i in array:
        count[i] += 1

    result = []
    for j in range(start, k+1):
        result += [j]* count[j]

    return result

input = [3,5,6,1,2,7,5]
print '%s\n%s\n' % (countingSort(input, 0, 10))

input = [18,5,100,3,1,19,6,0,7,4,2]
print '%s\n%s\n' % (countingSort(input))

input = [491, 55, 185, 468, 272, 91, 97, 398, 49, 163, 389, 91, 67, 82, 88, 497, 387, 93, 251, 265, 450, 287, 463, 17, 97, 53, 243, 226, 63, 374, 295, 199, 20, 258, 24, 60, 368, 143, 119, 372, 199, 251, 61, 261, 129, 199, 343, 66, 177, 218, 452, 302, 300, 79, 425, 93, 239, 363, 280, 188, 33, 285, 454, 177, 191, 253, 203, 386, 77, 371, 267, 207, 237, 246, 71, 226, 64, 432, 381, 4, 239, 36, 348, 241, 121, 191, 448, 289, 488, 23, 493, 317, 139, 177, 47, 171, 120, 323, 244, 191]
print '%s\n%s\n' % (countingSort(input, 0 , 500))