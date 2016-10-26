
def longest_subsequence(List):
    if len(List) < 1:
        return 0
    if len(List) < 2:
        return 1
    n = len(List)
    D = [0] * n
    D[n-1] = 1
    index_max = n-1
    max_so_far = 0
    for i in xrange(n-2, -1, -1):
        D[i] = 1
        for j in xrange(n-1, i, -1):
            if List[i] < List[j] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                if D[i] > max_so_far:
                    index_max = i
                    max_so_far = D[i]
    E = [List[index_max]]
    if max_so_far != 0:     # catch no increasing sequence found
        while D[index_max] > 1 and D[index_max] > D[index_max+1]:
            E.append(List[index_max+1])
            index_max += 1
    return len(E), E        # max of D is now the len of E

print longest_subsequence([7,5,6,1,2,7,5])

print longest_subsequence([4,5,6,1,2,7,5])

print longest_subsequence([7,6,4,3,2])

print longest_subsequence([1,2,3,4,5,6])

print longest_subsequence([-3,-2,-1,0,1,2,3])

print longest_subsequence([2,5,-2,0,3,4,3,1])

print longest_subsequence([4,3,2,1,2,3])

