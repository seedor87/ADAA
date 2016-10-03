import random

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

array = [18,5,100,3,1,19,6,0,7,4,2]
for i in range(1, len(array)+1):
    print "%s:\t"% ordinal(i), randomized_select(array, i)