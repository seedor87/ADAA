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

def permit_negatives(List, a, b, k=100):

    if a <= b:

        B = {}
        C = {}
        D = [0] * (k+k+2)
        for i in range(-k, k+1):
            B[i] = 0
            C[i] = 0

        for i in List:
            B[i] += 1

        C[-k] = B[-k]
        for i in range(-k+1, k+1):
            C[i] = B[i] + B[i-1]

        for i in range(-k, k+1):
            D[k+i] = C[i]
        print D

        return D[k+b] - D[k+(a-1)]

array = [8,7,4,5,3,1,5]
print actual_solution(array, 1, 6)

array = [0,0,1,2,5,7,11,17,21,56]
print actual_solution(array, 12, 16, k=100)
print actual_solution(array, 11, 56, k=100)

array = [18, 81, 37, 3, 76, 44, 79, 92, 62, 55, 27, 28, 0, 28, 16, 5, 11, 29, 6, 38, 21, 45, 90, 65, 81, 24, 92, 40, 60, 65, 48, 16, 32, 27, 39, 38, 57, 38, 18, 11, 14, 24, 82, 68, 15, 31, 40, 63, 12, 72, 82, 57, 67, 74, 35, 35, 85, 46, 29, 73, 75, 81, 86, 26, 1, 53, 33, 5, 32, 1, 71, 7, 66, 34, 6, 89, 27, 50, 4, 15, 28, 52, 98, 37, 93, 11, 42, 73, 22, 77, 25, 99, 47, 58, 97, 95, 47, 84, 71, 80]
print actual_solution(array, 10, 30, k=100)

array = [8, -64, -68, 58, 52, -77, 73, 30, -33, -45, -79, -87, 73, 90, -49, -57, 53, 18, 88, 50, -38, -45, -18, -11, -49, 60, 43, 58, -88, 98, -90, -1, -23, -53, 92, 53, 57, 43, 20, 19, -72, -90, -4, 33, -29, 40, 14, 57, -20, 15, 68, 100, -96, 92, -97, 85, 79, -43, 75, -90, -33, 1, 97, -52, 84, -19, 96, -83, -58, -27, 59, -99, -55, 18, 46, 60, 29, -73, 81, -64, 36, -40, 55, 23, 77, -78, -70, 66, 81, -99, -59, 35, -83, 51, 66, 53, 75, 12, -2, 86]
print permit_negatives(array, -100, 100, k=100)
