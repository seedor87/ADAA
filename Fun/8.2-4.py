array = [8,7,4,5,3,1,5]
k = 10
a = 1
b = 5

def prob8point2dash4(array, k, a, b):
    """
    The answer fo the problem 8.2-4
    """
    count = [0] * (k + 1)

    for i in array:
        count[i] += 1

    result = []
    for j in range(0, k + 1):
        result += [j] * count[j]

    return sum(count[a:b+1]), count[a:b+1]

print prob8point2dash4(array, k, a, b)




