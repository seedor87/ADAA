

RADIX = 10
def radixsort(List):
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]

        for  i in List:
            tmp = i / placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                List[a] = i
                a += 1

        placement *= RADIX

    return List


def main():

    input = [18,5,100,3,1,19,6,0,7,4,2]
    res = radixsort(input)
    print res

main()