def heapify(A):
    for root in xrange(len(A)//2-1, -1, -1):
        rootVal = A[root]
        child = 2*root+1
        while child < len(A):
            if child+1 < len(A) and A[child] > A[child+1]:
                child += 1
            if rootVal <= A[child]:
                break
            A[child], A[(child-1)//2] = A[(child-1)//2], A[child]
            child = child *2 + 1

list = [(3, "test3"),(1, "test1"),(2, "test2.1"),(4, "test4"),(6, "test6"),(2, "test2.2")]
while list:
    heapify(list)
    print list
    print list.pop(0)
print 'done'