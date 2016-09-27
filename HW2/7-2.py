i = 0
j = 0

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def dual_pivot_qs(List, start, top):
    if start < top:
        h, l, = dual_pivot_partition(List, start, top)
        dual_pivot_qs(List, start, h - 1)
        dual_pivot_qs(List, h + 1, l - 1)
        dual_pivot_qs(List, l + 1, top)
    return List

def dual_pivot_partition(List, start, top):

    p = start
    q = top
    k = p+1
    h = k
    l = q-1

    if List[p] > List[q]:
        exchange(List, p, q)

    while k <= l:
    # the last non-check index is l,as l+1 to top - 1 is the part III,
    #where all elements > list[top]
        if List[k] < List[p]:
            exchange(List, h, k)
            #h is the first element of part II
            h += 1
            #increase h by 1, for pointing to the first element of part II
            k += 1
            #increase k by 1, because we have checked list[k]
        elif List[k] > List[q]:
        #l is the last element of part IV
            exchange(List, l, k)
            #don't increase k, as we have not check list[l] yet
            l -= 1
            #after swap, we should compare list[k] with list[p] and list[q] again
        else: k += 1
        # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1#now,h is the last element of part I
    l += 1 #now, l is the first element of part III
    exchange(List, p, h)
    exchange(List, q, l)

    return h, l

input = [-40, 50, 0, 10, 20, -25, 5]

dual_pivot_qs(input, 0 , len(input)-1)

print input
