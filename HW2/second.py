from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' %(highlight, text, color.END)

def stringify(list):
    ret = '\n'
    for res in list:
        ret += "\t%s \tarray size %s:  \t%s sec\n" %(res[1], res[2], res[0])
    return ret

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
def quicksort(List):
    return _quicksort(List, 0, len(List)-1)

def _quicksort(List, p, r):
    if p < r:
       q = partition(List, p, r)
       _quicksort(List, p, q-1)
       _quicksort(List, q+1, r)
    return List


def partition(List, p, r):
    x = List[r]
    for j in range(p, r):
        if List[j] <= x:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

@timer
def random_quicksort(List):
    return _random_quicksort(List, 0, len(List)-1)

def _random_quicksort(List, p, r):
    if p < r:
        q = random_partition(List, p, r)
        _random_quicksort(List, p, q - 1)
        _random_quicksort(List, q + 1, r)
    return List

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
def quicksort2(List):
    return _quicksort2(List,0,len(List)-1)

def _quicksort2(List, p, r):
    if p < r:
       q = partition2(List, p, r)
       _quicksort2(List, p, q - 1)
       _quicksort2(List, q + 1, r)
    return List


def partition2(List, p, r):
   x = List[p]
   left = p + 1
   right = r

   while True:
       while left <= right and List[left] <= x:
           left = left + 1
       while List[right] >= x and right >= left:
           right = right - 1
       if right < left:
           break
       else:
           exchange(List, left, right)

   exchange(List, p, right)
   return right

@timer
def dual_pivot_qs(List):
    return _dual_pivot_qs(List, 0, len(List)-1)

def _dual_pivot_qs(List, p, r):
    if p < r:
        h, l, = Partition(List, p, r)
        # h, l, = dual_pivot_partition(List, p, r)
        _dual_pivot_qs(List, p, h - 1)
        _dual_pivot_qs(List, h + 1, l - 1)
        _dual_pivot_qs(List, l + 1, r)
    return List

def dual_pivot_partition(List, p, r):
    q, k = r, p + 1
    h = k
    l = q - 1

    if List[p] > List[q]:
        exchange(List, p, q)
    while k <= l:
        if List[k] < List[p]:
            exchange(List, h, k)
            h += 1
            k += 1
        elif List[k] > List[q]:
            exchange(List, l, k)
            l -= 1
        else:
            k += 1
    h -= 1
    l += 1
    exchange(List, p, h)
    exchange(List, q, l)

    return h, l

def Partition(array, start, end):
    copy = array[:]

    #print 'p', start, end

    x = array[end]
    i = start-1 # The end of the less than region.
    t = start-1
    for j in range(start, end):
        if array[j] == x:
            t+=1
            array[t], array[j] = array[j], array[t]
        if array[j] < x:
            i+=1
            t+=1
            array[i], array[j] = array[j], array[i]
    array[t+1], array[end] = array[end], array[t+1]
    # print copy, start, i+1, t+1, end, array
    return i+1, t

text = """Small Fixed Input fro Debugging""" + "-" * 1000
print text
input = [-40, 50, 0, 10, 20, -25, 5]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


text = """Size = 100, max, min = -10, 10""" + "-" * 1000
print text
input = [0, 10, 5, 3, 3, -5, -3, -3, 0, -8, -10, 1, 0, -7, 7, 10, 8, -9, -3, 2, 1, -7, -1, -7, -6, -4, -9, -1, -10, 7, -6, -9, 0, -2, 0, 4, -2, -10, -3, -7, 4, 7, 7, -1, -6, -2, 4, -4, -10, -4, -10, 8, -1, 6, -9, 0, -9, -2, -10, -4, 6, 3, -7, -9, 4, 9, 6, 0, 1, -3, 7, 0, -3, -10, 10, 5, -9, 3, -2, 7, 0, -9, 5, -7, 7, 9, -2, -7, -2, 2, 5, 7, 7, -5, 4, -7, -7, -3, -5, 9]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


text = """Size = 500, max, min = -10, 10""" + "-" * 1000
print text
input = [-9, -9, 9, 8, 0, -8, -9, -9, 10, 4, 1, 4, 8, 4, 4, -3, -10, -5, -3, 10, -6, 9, -7, -4, -6, -5, 7, -5, 10, -7, -5, 4, -9, 6, 2, -10, -2, -4, 0, -4, 6, -8, 4, 3, -6, 0, 9, 3, 10, -9, 0, 4, 8, -6, -2, 5, -10, 2, -6, -9, 2, -9, -7, 8, 3, -7, -7, -1, -4, 8, -9, -6, 5, 9, -3, -5, 3, 1, -1, 0, -10, -9, 2, -8, 0, 2, 6, 10, -8, 4, -9, 3, 3, 3, 4, -8, -9, 10, -6, 0, 9, 5, -10, 7, -7, -2, 0, 3, -6, 1, 9, 9, -8, -8, 2, -9, 5, -7, 3, 1, -3, 5, 3, 4, 2, -3, 7, -2, -7, 7, 0, 2, -4, -2, -2, 7, -8, -6, 6, 4, 8, -7, 4, -10, 8, 2, 0, 3, 9, -9, -1, -1, -9, 4, -7, -2, -7, 3, 0, 8, 1, 6, 2, 2, 1, -3, 4, -4, 0, 0, 5, -10, -10, -8, 3, -4, -4, -5, -2, 10, 6, -3, 0, 5, 5, -5, -6, -6, 6, -4, 1, 9, 1, 8, -6, 4, -2, -10, -3, -6, -6, -8, -1, 10, -5, 10, -5, -3, 3, 1, 9, 4, -6, 1, -7, 3, -5, -9, 8, 2, 3, -8, -4, -10, 8, -8, 8, -9, 4, -2, 9, 5, 8, -2, 1, 3, 2, -9, 8, 3, 6, -7, -3, -2, -3, 2, -7, -2, -6, 8, 9, -7, 3, -3, -10, 9, -1, 9, 10, -3, 6, -10, -5, 0, -10, 2, 1, 2, -5, 10, -7, 5, -7, 5, -4, 1, 2, -6, 4, 3, -1, 10, 6, 0, 2, -2, -9, 4, -6, -9, 9, -3, 4, -8, -4, 3, 1, 3, 5, 4, -1, -4, 6, 6, 0, 1, 3, 4, 5, 3, 3, 9, 10, 7, -6, 7, -6, 6, -2, -10, -1, 7, 0, -7, -2, 9, 10, 3, 9, 0, 5, 3, -4, -8, -3, 9, 1, -9, 1, 6, 8, -6, -10, 0, -1, 6, 6, -6, 8, 2, -8, 9, 10, 10, -5, -4, -6, 10, -1, 5, 0, 7, 8, -3, 8, 9, 8, 10, 6, -2, -9, 10, -9, 3, 7, -5, 3, -1, 3, -6, 4, 7, 7, -10, 4, 4, -7, 10, -10, -4, -10, -7, -3, 7, 2, -6, -2, -5, -8, -2, -2, -2, 10, -1, -9, 5, 7, 1, 1, 8, -6, 7, -7, -9, -9, -10, 2, 4, -5, 0, 7, -6, -3, -10, -8, 0, 6, 6, 3, -2, -1, 7, -4, 2, -4, 5, 2, -9, -3, -4, 0, 4, 10, -6, 5, 4, -5, 5, -7, 3, -9, -5, -3, -6, 2, 6, -9, 9, -4, -7, 7, 9, 6, -2, 8, 3, -5, -1, -10, 7, 7, -4, 0, -10, -8, -6, -7, 8, 1, -9, -1, 8, -5, 1, -3, 8, 6, 7, -5, 9, 5, 1, 0, 2, -5, 3, -1, 1, -2, -2]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


text = """Size = 100, max, min = -100, 100""" + "-" * 1000
print text
input = [-79, -46, 56, 26, -81, 88, -7, 98, 25, -79, 89, -34, 85, 88, 51, 42, 16, 32, 9, 78, 2, 20, -99, -65, 2, -72, -16, 87, -34, 46, 24, 65, -44, 5, -16, -85, -82, -97, 57, -15, -47, -19, 86, 64, -100, -2, -87, -72, -68, 19, -99, 14, -47, 98, -6, -38, -99, -29, 98, 42, 78, 26, -2, 94, 69, -83, 95, -21, 69, 34, -50, 0, 78, 36, 36, -93, 42, 54, 22, 79, 84, 66, -41, -92, -99, -28, -94, 29, 94, -55, 41, -65, -50, 59, -96, 95, 17, -39, 27, 77]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


text = """Size = 500, max, min = -100, 100""" + "-" * 1000
print text
input = [79, -67, -18, -44, 2, -97, 44, 73, -60, 99, 19, 100, 14, 3, -4, 48, 91, -15, -66, -28, -50, -21, 67, 96, -91, -6, -73, -49, 35, -49, 91, 96, -79, 35, -69, 9, 91, -20, 88, 84, -41, -37, -68, 93, -6, 55, -9, 49, 60, 26, -4, -41, -97, 79, -92, -86, 40, -85, -15, -98, 11, -24, 37, -96, -25, 21, -67, 23, 20, -86, 76, 75, -86, -58, -90, 39, 71, -19, 13, -70, -62, -19, 78, -60, -77, -91, -77, -52, -83, -48, -53, 65, 27, -9, -55, -40, -35, -77, -15, -73, -57, 13, 81, -20, -42, -54, -90, 9, 70, -58, -37, -36, 94, 90, 44, 95, -84, -5, 13, 86, -79, 6, 63, -92, -37, -81, 61, 47, 27, -15, -60, 48, 76, 40, -88, -54, -92, 42, 28, -74, -27, -78, -100, -87, -29, 21, 11, -89, -81, 45, 6, 92, 15, 47, 26, -65, 12, 39, -77, 33, 41, 7, -3, 67, -58, 47, -24, 20, 58, -100, -47, -81, -72, 96, -7, -24, -8, 37, -47, -48, 31, -15, 70, -93, -52, 96, -96, -76, -78, -57, 25, -82, -14, 46, 59, -100, -53, 84, -76, 67, -3, 87, -56, 90, -46, -15, -32, 3, 43, -67, -93, 74, 75, 47, -83, -23, -77, 7, -22, -96, 6, 84, 3, -83, 97, 36, -89, -95, -70, 6, -22, 6, -55, 29, -8, 15, -47, -78, 61, -75, -27, 93, -36, -41, 17, -50, -95, 91, -24, 17, 17, -29, 89, 26, 77, -76, 9, -20, -36, 11, 79, 65, -34, -98, -29, -74, 25, 42, -33, -87, 93, 19, -51, -69, 85, -4, 56, -36, 2, -47, -25, 72, -4, -43, 83, 79, -63, 42, -10, -55, 73, 94, 69, 90, 36, 92, 26, -38, 72, -40, 49, -25, 54, -41, 69, 77, -90, -100, 67, 21, -75, -44, 19, -99, 48, -20, 35, 71, -41, -39, -51, -57, -98, -77, 25, 2, -85, 56, 88, 65, 54, 71, 67, -10, 12, -59, -39, 9, -45, -52, -41, -93, -1, -22, -95, -2, -51, 65, -85, 73, 74, 12, -93, 61, 52, 76, -7, -67, 57, 84, 89, -30, -20, 66, -73, -58, 89, 37, -34, 48, -59, -94, 10, 82, 78, 28, 10, -23, 60, 93, 44, 90, -35, -47, 2, 60, 75, -96, 38, -13, -76, 95, 71, -37, -61, 3, 16, -7, -73, -20, -62, 23, -15, -92, -60, 91, -19, 45, -2, -55, 28, -50, 47, -40, -5, -41, -65, -95, -100, 54, 46, -2, -93, 32, 91, 1, 44, -15, 87, 72, 95, 38, 98, 53, -50, 85, -32, 12, 54, 76, 16, -98, -76, -80, 53, 32, 14, -100, -27, -8, -35, -58, 77, 100, -62, 93, -100, -41, -9, 32, 30, 49, 27, -11, 39, -45, -69, -64, 47, -58, -47, -14, 54, -68, 72, -14, -71, -59, -74, -63, 58, -46, -58, -30, 51, -25, 9, 99, 69, -95, -71, -69, 77, -88, 10, 66, -29, 90, -56, 9]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


text = """Size = 100, max, min = -500, 500""" + "-" * 1000
print text
input = [-428, -106, 10, 98, -319, -290, 277, -46, -290, -389, -420, 460, -434, -137, 13, -39, 374, -428, 128, 246, -136, 279, -215, -236, -424, -323, -221, -482, -332, -206, -496, 198, 310, 443, -107, 284, 102, 122, -243, 415, -303, 376, 435, -92, -139, -93, 353, -133, -243, -36, 215, -283, 51, -496, -388, -112, -141, 270, -453, 483, 193, -443, -160, -313, 18, -218, -400, 370, 323, 295, -469, 80, -270, -90, -95, 216, -63, -168, -498, -48, -8, 290, 167, 275, -408, 463, -455, 52, 247, 163, -401, 112, -485, -33, -339, -442, -115, 269, 137, -386]

res = quicksort(input)
print res

res = random_quicksort(input)
print res

res = quicksort2(input)
print res

res = dual_pivot_qs(input)
print res


sys.exit(0)

text = """Size = 100, max, min = 1,1""" + "-" * 1000
print text

count = 0
summ = 0
for i in range(0, 1000):
    input = [1] * 100

    res = random_quicksort(input)
    print res
    summ += res[1]
    count +=1

print color.GREEN + str(summ/count) + color.END