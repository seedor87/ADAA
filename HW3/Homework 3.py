import random

def preprocess_solution(a,k=9):
    print [x for x in range(0,10)]
    k+=1
    counts = [0] * k
    for i in range(0,len(a)):
        counts[a[i]] += 1
    print counts
    for i in range(1, k):
        counts[i] += counts[i-1]
    print counts

    output = [0] * (len(a)+1)
    for i in range(len(a)-1, -1, -1):
        output[counts[a[i]]] = a[i]
    return output[1:], counts

def run(output, count):
    # print [x for x in range(1,10)]
    # print count
    print output
    while 1:
        x = raw_input("Index a and index b: ")
        x = x.split()
        print count[int(x[1])] - count[int(x[0])-1]

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def Partition(List, p=0, r=None) :
    if r is None: r = len(List)-1
    x = List[r]
    i = p-1
    for j in range(p, r):
        if List[j] <= x:
            i = i +1
            exchange(List,i,j)
    exchange(List, i+1, r)
    return i+1

def randSelect(A, i):
    while len(A) > 1:
        mid = Partition(A)
        k = len(A[:mid])+1
        if k == i: return A[mid]
        elif i < k: A = A[:mid]
        else:
            A = A[mid+1:]
            i-=k
    return A[0]


array = [8,9,4,5,3,1,7]
# run(*preprocess_solution(array))
print randSelect(array, 2)