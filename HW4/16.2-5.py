
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

def solver(List, n=2, sort=False):

    def print_res(S, n):
        if isinstance(S, dict):
            for key, val in S.iteritems():
                print '%s<%s:\t%s' % (key, key+n, val)
        else:
            for i in range(len(S)):
                print '%s<%s:\t%s' % (i,i+n, S[i])

    def method_A(List, n): # Method A - works on unsorted array
        lim = (int(List[-1])) / n
        S = {}
        for i in range(lim + 1):
            S[i*n] = []

        for i in List:
            S[n*int(i/n)].append(i)
        print_res(S, n)

    def method_B(List, n): # Method B - works only on sorted array
        lim = (int(List[-1])) / n
        s = {}
        for i in range(lim+1):
            s[i*n] = []

        index = 0
        for i in List:
            if i >= index + n:
                while i >= index + n:
                    index += n
            s[index].append(i)
        print_res(s, n)

    if len(List) > 0:
        if sort:
            List_ = quicksort(List)
        else:
            List_ = List
        method_B(List_, n)
        print '- - ' * 25
        method_A(List_, n)
    else:
        print "--Empty List--"

n = 1
solver([0.0, 0.1, 3.0], n)
print "=" * 100
solver([0.7, 1.0, 2.3, 2.6, 2.9, 3.0, 3.1, 3.6, 3.9, 4.2, 4.7, 5.2, 5.5, 10.0, 10.1], n)
print "=" * 100
solver([3.5], n)
print '=' * 100
solver([])

