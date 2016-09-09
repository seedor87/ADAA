# algorithms for max_sub_array finding
from __future__ import division
import sys, operator, time, doctest
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
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1 - t0))
               )
        return result
    return func_timer

@timer
def Brute_Force(L):
    max = []
    for i in range(0,len(L)):
        for j in range(i, len(L)):
            if sum(L[i:j]) > sum(max):
                max = L[i:j]
    if sum(L) > sum(max):
        return L
    return max

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
            L_low, L_high, L_sum = Find_Max_Sub_Array(L, low, mid)
            R_low, R_high, R_sum = Find_Max_Sub_Array(L, mid+1, high)
            C_low, C_high, C_sum = Find_Max_Crossing_Sub_Array(L, low, mid, high)
        return max(L_sum, R_sum, C_sum)

    return Find_Max_Sub_Array(L, 0, len(L))

def div_and_conquer(L):
    def crossingsubarray(A, low, mid, high):

        negetiveinfinity = -10000000000
        summ = 0
        for i in range(mid, low - 1, -1):
            summ = summ + A[i]
            if summ > negetiveinfinity:
                negetiveinfinity = summ
                leftindex = i
        left = negetiveinfinity


        negetiveinfinity = -10000000000
        summ = 0

        for j in range(mid+1, high+1):
            summ = summ + A[j]
            if summ > negetiveinfinity:
                negetiveinfinity = summ
                rightindex = j
        right = negetiveinfinity

        return(leftindex, rightindex, left + right)

    def findmaxarray(alist, low, high):

        if high == low:
            return low, high, alist[low]

        else:

            mid = (low+high)//2

            leftlow, lefthigh, leftsum = findmaxarray(alist, low, mid)
            rightlow, righthigh, rightsum = findmaxarray(alist, mid + 1, high)
            crosslow, crosshigh, crosssum = crossingsubarray(alist, low, mid, high)

            if leftsum >= rightsum and leftsum >= crosssum:
                return leftlow, lefthigh, leftsum
            elif rightsum >= leftsum and rightsum >= crosssum:
                return rightlow, righthigh, rightsum
            else:
                return crosslow, crosshigh, crosssum

    @timer
    def run(L):
        return findmaxarray(L, 0, len(L)-1)

    return run(L)

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

    input = list_rand_int(Lim=10, Len=10, Sign=-1)
    print input

    result = Brute_Force(input)
    print result, sum(result)

    L,H,maxi = div_and_conquer(input)
    print input[L:H+1], maxi

    result = Kadanes_Method(input)
    print result, sum(result)

    sys.exit(0)
