# algorithms for max_sub_array finding

from __future__ import division
import sys, time, doctest
from random import randint, uniform
from functools import wraps

# my_round = lambda L, D: [round(i, D) for i in L ]
# ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # toy for interpretation

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]
list_rand_float = lambda Lim, Len, Sign=0: [uniform(Sign*Lim,Lim) for x in range(0,Len)]

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %(function.func_name, str(t1 - t0)))
        return result
    return func_timer

@timer
def Brute_Force(L):
    res = []
    for i in range(0,len(L)+1):
        for j in range(i, len(L)+1):
            if sum(L[i:j]) > sum(res):
                res = L[i:j]
    if sum(L) > sum(res):
        return L
    return res

@timer
def Div_And_Conq(L):

    def Find_Max_Crossing_Sub_Array(L, low, mid, high):
        L_sum, R_sum = -sys.maxint - 1, -sys.maxint - 1
        max_left = max_right = sum = 0
        for i in range(mid, low-1, -1):
            sum = sum + L[i]
            if sum > L_sum:
                L_sum, max_left = sum, i
        sum = 0
        for j in range(mid+1, high+1, 1):
            sum = sum + L[j]
            if sum > R_sum:
                R_sum, max_right = sum, j
        return max_left, max_right, L_sum+R_sum

    def Find_Max_Sub_Array(L, low, high):
        if high == low:
            return low, high, L[low]
        else:
            mid = (low+high) // 2

            """this is slightly slower than the triple check if's"""
            lst = []
            lst.extend(Find_Max_Sub_Array(L, low, mid))
            lst.extend(Find_Max_Sub_Array(L, mid+1, high))
            lst.extend(Find_Max_Crossing_Sub_Array(L, low, mid, high))
            indx_res = lst.index(max(lst[2], lst[5], lst[8]))
            return lst[indx_res-2], lst[indx_res-1], lst[indx_res]

            """this is slightly faster than the aforementioned"""
            # L_low, L_high, L_sum = Find_Max_Sub_Array(L, low, mid)
            # R_low, R_high, R_sum = Find_Max_Sub_Array(L, mid+1, high)
            # C_low, C_high, C_sum = Find_Max_Crossing_Sub_Array(L, low, mid, high)
            # if L_sum >= R_sum and L_sum >= C_sum:
            #     return L_low, L_high, L_sum
            # elif R_sum >= L_sum and R_sum >= C_sum:
            #     return R_low, R_high, R_sum
            # else:
            #     return C_low, C_high, C_sum

    low,high,i = Find_Max_Sub_Array(L, 0, len(L)-1)
    return L[low:high+1]

@timer
def Kadanes_Method(L):
    best_so_far = cur_best = curi = starti = besti = 0
    for i in range(0, len(L)):
        if cur_best + L[i] > 0:
            cur_best += L[i]
        else:
            cur_best, curi = 0, i+1

        if cur_best > best_so_far:
            starti, besti, best_so_far = curi, i+1, cur_best
    return L[starti:besti]

def main(Lim, Len):
    """
    >>> main(10, 100)
    1
    >>> main(10, 1000)
    1
    >>> main(10, 2000)
    1
    """
    input = list_rand_int(Lim=Lim, Len=Len, Sign=-1)
    result = Brute_Force(input)
    print input
    print result
    return 1

if __name__ == '__main__':

    input = list_rand_int(Lim=10, Len=50, Sign=-1)
    print input

    result = Brute_Force(input)
    print result, sum(result)

    result = Div_And_Conq(input)
    print result, sum(result)

    result = Kadanes_Method(input)
    print result, sum(result)

    sys.exit(0)
