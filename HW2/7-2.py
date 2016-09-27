

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def dual_pivot_qs(List):
    return _dual_pivot_qs(List, 0, len(List)-1)

def _dual_pivot_qs(List, p, r):
    if p < r:
        h, l, = dual_pivot_partition(List, p, r)
        _dual_pivot_qs(List, p, h - 1)
        _dual_pivot_qs(List, h + 1, l - 1)
        _dual_pivot_qs(List, l + 1, r)
    return List

def dual_pivot_partition(List, p, r):

    p, q, k  = p, r, p+1
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

res = dual_pivot_qs(input)

print res

input = [-428, -106, 10, 98, -319, -290, 277, -46, -290, -389, -420, 460, -434, -137, 13, -39, 374, -428, 128, 246, -136, 279, -215, -236, -424, -323, -221, -482, -332, -206, -496, 198, 310, 443, -107, 284, 102, 122, -243, 415, -303, 376, 435, -92, -139, -93, 353, -133, -243, -36, 215, -283, 51, -496, -388, -112, -141, 270, -453, 483, 193, -443, -160, -313, 18, -218, -400, 370, 323, 295, -469, 80, -270, -90, -95, 216, -63, -168, -498, -48, -8, 290, 167, 275, -408, 463, -455, 52, 247, 163, -401, 112, -485, -33, -339, -442, -115, 269, 137, -386]

res = dual_pivot_qs(input)

print res
