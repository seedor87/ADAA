from random import randint

list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

def actual_solution(List, a, b, k=10):

    if a <= b:

        B = C = [0] * (k+1)

        for i in List:
            B[i] += 1

        C[0] = B[0]
        for i in range(1, k+1):
            C[i] = B[i] + B[i-1]

        return C[b] - C[a-1]

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

array = [8,9,4,5,3,1,7]
# print actual_solution(array, 1, 6)
#
# array = [0,0,1,2,5,7,11,17,21,56]
# print actual_solution(array, 12, 16, k=100)
# print actual_solution(array, 11, 56, k=100)
#
# array = [18, 81, 37, 3, 76, 44, 79, 92, 62, 55, 27, 28, 0, 28, 16, 5, 11, 29, 6, 38, 21, 45, 90, 65, 81, 24, 92, 40, 60, 65, 48, 16, 32, 27, 39, 38, 57, 38, 18, 11, 14, 24, 82, 68, 15, 31, 40, 63, 12, 72, 82, 57, 67, 74, 35, 35, 85, 46, 29, 73, 75, 81, 86, 26, 1, 53, 33, 5, 32, 1, 71, 7, 66, 34, 6, 89, 27, 50, 4, 15, 28, 52, 98, 37, 93, 11, 42, 73, 22, 77, 25, 99, 47, 58, 97, 95, 47, 84, 71, 80]
# print actual_solution(array, 10, 30, k=100)
#
