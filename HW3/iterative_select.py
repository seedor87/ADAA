from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps
import matplotlib.pyplot as plt


list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # toy for interpretation

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

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def random_partition(List, p, r) :
    x = p + random.randrange(r - p + 1)
    exchange(List, x, r)
    for j in range(p, r):
        if List[j] <= List[r]:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p

@timer
def randomized_select(List, i):
    try:
        start = 0
        end = len(List)-1
        while start < end:
            q = random_partition(List, start, end)
            k = q - start + 1
            if i == k:
                return List[q]
            elif i < k:
                end = q - 1
            else:
                start = q + 1
                i = i - k
        return List[start]
    except Exception as e:
        return e

@timer
def sort_then_select(List, i):
    return _quicksort(List, 0, len(List)-1)[i-1]

def _quicksort(List, p, r):
    if p < r:
        q = random_partition(List, p, r)
        _quicksort(List, p, q - 1)
        _quicksort(List, q + 1, r)
    return List

print """Test 1: control input for debugging""" + '-' * 100
array = [18,5,100,3,1,19,6,0,7,4,2]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[0], color='green')

plt.show()

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[0], color='red')

plt.show()


print """Test 2: randomly generated test input for timing""" + '-' * 100
array = [-62, -32, 89, 72, -76, -11, 54, -32, -63, 12, 11, 60, 32, -27, 32, 17, -85, -49, -3, 27, -71, 52, -21, -49, 5, -12, 4, -67, 45, 54, -55, 84, 74, 78, -32, 23, 74, 73, 57, 81, -5, 98, 51, 18, 73, -90, 10, -71, 41, -93, -92, 36, -26, -94, -33, -75, 55, 55, 18, 29, -39, -15, -70, 85, -35, 20, 89, -93, -63, -46, 70, 60, -82, -86, 41, 40, 73, 38, 28, 35, -87, -72, 8, 7, -26, -97, 5, -44, 83, 66, -87, 82, 83, -65, 14, -87, 19, -78, 69, -4]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[0], color='green')

plt.show()

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[0], color='red')

plt.show()
