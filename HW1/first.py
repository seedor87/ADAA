# algorithms for max_sub_array finding

from __future__ import division
import sys, timeit
from random import randint, uniform
from functools import wraps
import sys

# my_round = lambda L, D: [round(i, D) for i in L ]
# ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # toy for interpretation

"""
The following are tools used to emphasize the provided results in console prints
"""
list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]
list_rand_float = lambda Lim, Len, Sign=0: [uniform(Sign*Lim,Lim) for x in range(0,Len)]

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

"""
The following are the three methods used to solve for the max sub-array, using first brute force, then divide and conquer, and finally a linear solution.
"""
@timer
def Brute_Force(L):
    """
    answer to question 3: the brute force method for finding max sub array
    """
    res = []
    for i in range(0,len(L)+1):
        for j in range(i, len(L)+1):
            if sum(L[i:j]) > sum(res):
                res = L[i:j]
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

            index_of_result = lst.index(max(lst[2], lst[5], lst[8]))
            return lst[index_of_result-2], lst[index_of_result-1], lst[index_of_result]

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

    if len(L) < 2:  # check to make sure the array is of adequate size to be operated on
        return L
    low, high, i = Find_Max_Sub_Array(L, 0, len(L)-1)
    return L[low:high+1]

@timer
def Linear_Method(L):
    """
    This is the solution to the final question of the homework, question 5.
    The linear time solution to the max sub-array problem
    """
    best_so_far = L[0]
    cur_best = finalStart = finalEnd= start_index = 0
    for i in range(0, len(L)):
        if cur_best + L[i] > 0:
            cur_best += L[i]
        else:
            cur_best, finalStart = 0, i+1
        if cur_best > best_so_far:
            start_index, finalEnd, best_so_far = finalStart, i + 1, cur_best
    return L[start_index:finalEnd]

@timer
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    cur_index = start_index = 0
    for x in A[1:]:
        if max_ending_here + x > x:
            max_ending_here = max_ending_here + x
            start_index = cur_index
        else:
            max_ending_here = x
            start_index = cur_index
        max_so_far = max(max_so_far, max_ending_here)
        cur_index += 1
    return max_so_far, start_index

@timer
def main(lim, method=Linear_Method):

    input = list_rand_int(Lim=10, Len=lim, Sign=-1)
    # input = [-5, 100, -500, -10, 50, -60, 800] # Sample Input
    result, run_time = method(input)
    print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)
    return run_time

if __name__ == '__main__':

    lim_step= 10
    results = []
    test_array_sizes = [x * lim_step for x in range(1,11)]
    for i in test_array_sizes:
        results.append((main(lim=i, method=Brute_Force)[1], Brute_Force.__name__, i))
        results.append((main(lim=i, method=Div_And_Conq)[1], Div_And_Conq.__name__, i))
        results.append((main(lim=i, method=Linear_Method)[1], Linear_Method.__name__, i))

    print wrap_text("Total Run-times: %s" % (stringify(results)), color.GREEN)


    """Code to display plot for visual evaluation of runtime values"""
    try:
        import matplotlib.pyplot as plt

        runtime_results = [x[0] for x in results]

        plt.plot(test_array_sizes, runtime_results[0::3], ".r-")
        plt.plot(test_array_sizes, runtime_results[1::3], ".y-")
        plt.plot(test_array_sizes, runtime_results[2::3], ".g-")
        plt.show()
    except Exception as e:
        sys.stderr.write('Check Dependencies\n')
        sys.stderr.write(str(e)+ '\n')


    """test to show independent usage"""
    """Note the usage;
            Len=50 -> input array of length 50
            Lim=10 -> input array will be of integers between -10 and 10
    """
    # input = list_rand_int(Lim=10, Len=50, Sign=0)
    # print input
    #
    # result, run_time = Brute_Force(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)
    # result, run_time = Div_And_Conq(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)
    # result, run_time = Linear_Method(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)

    """Tests on input = []"""
    # input = []
    #
    # result, run_time = Brute_Force(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)
    # result, run_time = Div_And_Conq(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)
    # result, run_time = Linear_Method(input)
    # print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED)

    """Test on uniform input to reflected accurately measure runtime"""
    """NOTE: input is same across all runs"""
    input = [-9, 9, 2, 5, -8, 8, 2, -6, -10, 5, 2, -6, -9, 1, 2, 10, -5, 9, 9, 3, -7, 8, 1, 6, -3, -9, -7, 7, 7, 7, 10, 10, 0, 6, -2, -6, 4, 5, -4, 5, -5, 1, 9, -4, -10, 8, -3, -1, 1, 8, 10, 10, 6, 10, 5, 10, 5, -10, -9, -8, -9, 10, -2, 5, 9, 0, -5, 6, 10, -9, 9, -7, 0, -1, -6, 10, -8, 4, -3, -5, 6, 2, -10, 5, 7, 0, -6, -2, -10, 2, -1, 8, 2, 1, 8, -7, 7, -8, 8, -6]
    print "input:", input

    runtime_results = []
    for i in range(0, 5):
        result, run_time = Brute_Force(input)
        runtime_results.append(run_time)
        print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED), "runtime:", run_time
        result, run_time = Div_And_Conq(input)
        runtime_results.append(run_time)
        print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED), "runtime:", run_time
        result, run_time = Linear_Method(input)
        runtime_results.append(run_time)
        print "ar:", result, '\n', 'Sum', wrap_text(sum(result), color.RED), "runtime:", run_time

    try:
        import matplotlib.pyplot as plt
        test_array_sizes = [1,2,3,4,5]

        plt.plot(test_array_sizes, runtime_results[0::3], ".r-")
        plt.plot(test_array_sizes, runtime_results[1::3], ".y-")
        plt.plot(test_array_sizes, runtime_results[2::3], ".g-")
        plt.show()
    except Exception as e:
        sys.stderr.write('Check Dependencies\n')
        sys.stderr.write(str(e)+ '\n')

    input = [-2,-3,-1]
    print max_subarray(input)

    sys.exit(0)
