
def solution_non_negatives(array, a, b, k=10):

    if a <= b:
        count = [0] * (k + 1)

        for i in array:
            count[i] += 1

        return sum(count[a:b+1]), zip(xrange(a, b+1), count[a:b+1])
    else:
        raise Exception('Invalid Indices')

def solution_allows_negatives(array, a, b, k =10):

    if a <= b:
        count ={}
        for i in range(-k, k):
            count[i] = 0

        for i in array:
            count[i] += 1

        res = 0
        ret = []
        for i in range(a, b+1):
            res += count[i]
            ret.append((i, count[i]))
        return res, ret
    else:
        raise Exception('Invalid Indices, %s not <= %s' % (a, b))

try:
    array = [8,7,4,5,3,1,5]
    print solution_non_negatives(array, 3, 2)
except Exception as e:
    print e

array = [8,7,4,5,3,1,5]
print solution_non_negatives(array, 4, 6)

array = [-1,1,-2,-3,3,2,1]
print solution_allows_negatives(array, -2, 2)

array = [-62, -32, 89, 72, -76, -11, 54, -32, -63, 12, 11, 60, 32, -27, 32, 17, -85, -49, -3, 27, -71, 52, -21, -49, 5, -12, 4, -67, 45, 54, -55, 84, 74, 78, -32, 23, 74, 73, 57, 81, -5, 98, 51, 18, 73, -90, 10, -71, 41, -93, -92, 36, -26, -94, -33, -75, 55, 55, 18, 29, -39, -15, -70, 85, -35, 20, 89, -93, -63, -46, 70, 60, -82, -86, 41, 40, 73, 38, 28, 35, -87, -72, 8, 7, -26, -97, 5, -44, 83, 66, -87, 82, 83, -65, 14, -87, 19, -78, 69, -4]
print solution_allows_negatives(array, -50, 50, k=100)




