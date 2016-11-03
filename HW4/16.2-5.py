
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
        for key, val in S.iteritems():
            print '%s->%s:\t%s' % (key, key+1, val)

    n = len(List)
    # first sort to obtain a list y
    Y = quicksort(List)
    lim = int(Y[-1]) + 1

    # S is list of numbers that are bucket sorted in to the key corresponding gto their floor division
    S ={}
    for i in range(lim):
        S[i] = []

    for i in Y:
        S[int(i)].append(i)

    # # For each element i in Y, if i < current index of s, add to list at index of s, else increment index and add it to next
    # index = 1
    # for i in Y:
    #     if i < index:
    #         S[index-1].append(i)
    #     elif i == index:
    #         index += 1
    #         S[index - 1].append(i)
    #     else: # i > index
    #         index += int(i)
    #         S[index - 1].append(i)

    print_res(S)

solver([0.0, 1.2, 3.0])
solver([0.7, 1.0, 3.0, 2.9, 10.1, 2.3, 2.6, 3.1, 3.6, 3.9, 4.7, 4.2, 10.0, 5.2, 5.5])

