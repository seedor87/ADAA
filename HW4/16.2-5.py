
def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def partition(List, p, r):
    x = List[r]
    for j in range(p, r):
        if List[j] <= x:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p

def quicksort(List):
    return _quicksort(List, 0, len(List)-1)

def _quicksort(List, p, r):
    if p < r:
       q = partition(List, p, r)
       _quicksort(List, p, q-1)
       _quicksort(List, q+1, r)
    return List

def solver(List):

    def print_res(S):
        if isinstance(S, dict):
            for key, val in S.iteritems():
                print '%s<%s:\t%s' % (key, key+1, val)
        else:
            for i in range(len(S)):
                print '%s<%s:\t%s' % (i,i+1, S[i])

    def method_A(List): # Method A - works on unsorted array
        S = []
        for i in range(int(max(List))+1):
            S.append([])
        for i in List:
            S[int(i)].append(i)
        print_res(S)

    def method_B(List): # Method B - works only on sorted array
        lim = int(List[-1]) + 1
        S = {}
        for i in range(lim):
            S[i] = []

        index = 0
        for i in List:
            if i >= index+1:
                while i >= index + 1:
                    index += 1
            S[index].append(i)
        print_res(S)

    if len(List) > 0:
        method_B(List)
    else:
        print "--Empty List--"

solver([0.0, 0.1, 3.0])
print '-' * 100
solver([0.7, 1.0, 2.3, 2.6, 2.9, 3.0, 3.1, 3.6, 3.9, 4.2, 4.7, 5.2, 5.5, 10.0, 10.1])
print '-' * 100
solver([3.5])
print '-' * 100
solver([])

