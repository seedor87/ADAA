"""This method will work to return the result of the categorization of as a python dictoinary"""

def solutionA(A, n=1):
    S = {}
    if A:
        index, i, total = 0,0,1
        at_A = A[index]
        S[at_A] = []
        for i in A:
            if i > at_A + n:
                total += 1
                at_A = i
                S[at_A] = []
            S[at_A].append(i)
    for k, v in S.iteritems():
        print '%s<%s:\t%s' % (k, k+n, v)

def solutionB(A, n=1):
    lim = (int(A[-1])) / n      # lim = int(A[A.length -1])
    S = [0 for _ in range((lim+1)*n)]   # let s be a new array of length [lim+1], whose elements are new empty queues
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

    index = 0
    for elem in S:
        if elem < 1:
            pass
        else:
            print '@: %s<%s' % (index,index+n)
        index += 1
    return total

solutionA([0.7, 1.0, 2.3, 2.6, 2.9, 3.0, 3.1, 3.6, 3.9, 4.2, 4.7, 5.2, 5.5, 10.0, 10.1])

solutionB([0.7, 1.0, 2.3, 2.6, 2.9, 3.0, 3.1, 3.6, 3.9, 4.2, 4.7, 5.2, 5.5, 10.0, 10.1])
