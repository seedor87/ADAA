# algorithms for max_sub_array finding
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

    input = list_rand_int(Lim=10, Len=100, Sign=-1)
    result = Brute_Force(input)
    print input
    print result
    sys.exit(0)
