
def longest_subsequence(A):
    if len(A) < 1:
        return 0
    if len(A) < 2:
        return 1

    n = len(A) # A.length
    D = [0] * n # let D be new array of length 1 to n
    D[n-1] = 1
    index_max = n-1 # tracking index of max value so far
    max_so_far = 0 # value of max so far
    for i in xrange(n-2, -1, -1): # for i = n-2 down to 0, inclusive
        D[i] = 1
        for j in xrange(n-1, i, -1): # for j in range j= n-1 down to i, exclusive
            if A[i] < A[j] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                if D[i] > max_so_far: # new value > max so far...
                    index_max = i       # set tracking index and new max so far
                    max_so_far = D[i]

    E = [A[index_max]] # let E be new list of one element, A[index of final max so far]
    ret_len = 1
    if max_so_far != 0:     # catch no increasing sequence found
        while D[index_max] > 1 and D[index_max] > D[index_max+1]: # print 'len seq: %s, seq: %s' % sub list of A that is longest increasing sub-sequence
            E.append(A[index_max + 1])
            index_max += 1
            ret_len += 1
        return ret_len, E  # length of longest increasing subsequence of A (max of D), is now the len of E
    else:
        return ret_len, [] # empty list denotes no increasing subseq. of length > 2

print 'len seq: %s, seq: %s' % longest_subsequence([7,5,6,1,2,7,5])

print 'len seq: %s, seq: %s' % longest_subsequence([4,5,6,1,2,7,5])

print 'len seq: %s, seq: %s' % longest_subsequence([7,6,4,3,2])

print 'len seq: %s, seq: %s' % longest_subsequence([1,2,3,4,5,6])

print 'len seq: %s, seq: %s' % longest_subsequence([-3,-2,-1,0,1,2,3])

print 'len seq: %s, seq: %s' % longest_subsequence([2,5,-2,0,3,4,3,1])

print 'len seq: %s, seq: %s' % longest_subsequence([4,3,2,1,2,3])

