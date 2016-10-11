
from __future__ import division
import sys, timeit
from random import randint, uniform
from functools import wraps

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

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

    count = {}
    for i in range(-k, k+1):
        count[i] = 0

    for i in array:
        count[i] += 1

    result = []
    for j in range(start, k+1):
        result += [j]* count[j]

    return result

input = [3,5,6,1,2,7,5]
print '%s\n%s\n' % (countingSort(input, k=10))

input = [18,5,100,3,1,19,6,0,7,4,2]
print '%s\n%s\n' % (countingSort(input))

input = [491, 55, 185, 468, 272, 91, 97, 398, 49, 163, 389, 91, 67, 82, 88, 497, 387, 93, 251, 265, 450, 287, 463, 17, 97, 53, 243, 226, 63, 374, 295, 199, 20, 258, 24, 60, 368, 143, 119, 372, 199, 251, 61, 261, 129, 199, 343, 66, 177, 218, 452, 302, 300, 79, 425, 93, 239, 363, 280, 188, 33, 285, 454, 177, 191, 253, 203, 386, 77, 371, 267, 207, 237, 246, 71, 226, 64, 432, 381, 4, 239, 36, 348, 241, 121, 191, 448, 289, 488, 23, 493, 317, 139, 177, 47, 171, 120, 323, 244, 191]
print '%s\n%s\n' % (countingSort(input, k=500))

input = [8, -64, -68, 58, 52, -77, 73, 30, -33, -45, -79, -87, 73, 90, -49, -57, 53, 18, 88, 50, -38, -45, -18, -11, -49, 60, 43, 58, -88, 98, -90, -1, -23, -53, 92, 53, 57, 43, 20, 19, -72, -90, -4, 33, -29, 40, 14, 57, -20, 15, 68, 100, -96, 92, -97, 85, 79, -43, 75, -90, -33, 1, 97, -52, 84, -19, 96, -83, -58, -27, 59, -99, -55, 18, 46, 60, 29, -73, 81, -64, 36, -40, 55, 23, 77, -78, -70, 66, 81, -99, -59, 35, -83, 51, 66, 53, 75, 12, -2, 86]
print '%s\n%s\n' % (countingSort(input, start=-100, k=100))