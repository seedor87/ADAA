
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

    def print_res_A_B(S, n):
        if isinstance(S, dict):
            for key, val in S.iteritems():
                print '%s<%s:\t%s' % (key, key+n, val)
        else:
            for i in range(len(S)):
                index = int(S[i][0])
                print '%s<%s:\t%s' % (index,index+n, S[i])

    def print_res_C(S):
        index = 0
        for elem in S:
            if elem < 1:
                pass
            else:
                print '@: %s<%s' % (index,index+1)
            index += 1

    def method_A(A, n): # Method A - works on unsorted array
        lim = (int(A[-1])) / n
        S = {}
        for i in range(lim + 1):
            S[i*n] = []

        for i in A:
            S[n*int(i/n)].append(i)
        return S

    def method_B(A, n): # Method B - works only on sorted array
        lim = (int(A[-1])) / n      # lim = int(A[A.length -1])
        s = {}                      # let s be a new array of length [lim+1], whose elements are new empty queues
        for i in range(lim+1):
            s[i*n] = []

        index = 0
        for i in A:                 # loop in O(n)
            if i >= index + n:      # this loop only fills in the incrementing of the value index to match closest bounding integer
                while i >= index + n:
                    index += n      # total, across all elements, of this is O(k), where k is the int(lim) + 1
            s[index].append(i)
        return s

    def method_C(A, n):  # Method C - works only on sorted array
        lim = (int(A[-1])) / n      # lim = int(A[A.length -1])
        S = [0 for _ in range(lim+1)]   # let s be a new array of length [lim+1], whose elements are new empty queues
        total = 0
        index = 0
        for i in A:
            if i >= index + n:  # this loop only fills in the incrementing of the value index to match closest bounding integer
                while i >= index + n:
                    index += n
            if S[index] > 0:
                pass
            else:
                S[index] += 1
                total += 1
        print_res_C(S)
        return total

    def method_D(A, n):
        lim = (int(A[-1])) / n  # lim = int(A[A.length -1])
        S = [0 for _ in range(lim+1)]   # let s be a new array of length [lim+1], whose elements are new empty queues
        index, i, total = 0,0,0
        while i < len(A):
            S[index] += 1
        print_res_C(S)
        return total

    if len(List) > 0:
        if sort:
            List_ = quicksort(List)
        else:
            List_ = List
        print 'Method B, answer to question:'
        s = method_B(List_, n)
        print_res_A_B(s, n)
        print '- - ' * 25
        print 'Method A, fastest, works on unsorted array:'
        s = method_A(List_, n)
        print_res_A_B(s, n)
        print '- - ' * 25
        print 'Method C, works to provide only most reduced solution:'
        print 'total unit length indecies:\n', method_C(List_, n)
        print '- - ' * 25
        print 'Method D:\n'
        print method_D(List_, n)
    else:
        print "--Empty List--"

n = 1
solver([0.0, 2.1, 3.0], n)
print "=" * 100
solver([0.7, 1.0, 2.3, 2.6, 2.9, 3.0, 3.1, 3.6, 3.9, 4.2, 4.7, 5.2, 5.5, 10.0, 10.1], n)
print "=" * 100
solver([3.5], n)
print '=' * 100
solver([])

