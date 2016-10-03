import random
from random import randint

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # toy for interpretation

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

def randomized_select(List, i):
    try:
        begin = 0
        end = len(List)-1
        while begin < end:
            q = random_partition(List, begin, end)
            k = q - begin + 1
            if i == k:
                return List[q]
            elif i < k:
                end = q -1
            else:
                begin = q+1
                i = i -k
        return List[begin]
    except Exception as e:
        return e


print """Test 1""" + '-' * 100
array = [18,5,100,3,1,19,6,0,7,4,2]
for i in range(1, len(array)+1):
    print "%s:\t"% ordinal(i), randomized_select(array, i)

print """Test 2""" + '-' * 100
array = [-62, -32, 89, 72, -76, -11, 54, -32, -63, 12, 11, 60, 32, -27, 32, 17, -85, -49, -3, 27, -71, 52, -21, -49, 5, -12, 4, -67, 45, 54, -55, 84, 74, 78, -32, 23, 74, 73, 57, 81, -5, 98, 51, 18, 73, -90, 10, -71, 41, -93, -92, 36, -26, -94, -33, -75, 55, 55, 18, 29, -39, -15, -70, 85, -35, 20, 89, -93, -63, -46, 70, 60, -82, -86, 41, 40, 73, 38, 28, 35, -87, -72, 8, 7, -26, -97, 5, -44, 83, 66, -87, 82, 83, -65, 14, -87, 19, -78, 69, -4]
for i in range(1, len(array)+1):
    print "%s:\t"% ordinal(i), randomized_select(array, i)