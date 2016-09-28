import random

global qcCalls, ptCalls, qcrCalls, ptrCalls
qcCalls = 0
ptCalls = 0
qcrCalls = 0
ptrCalls = 0

def Quicksort(array, start, end):
    global qcCalls, ptCalls, qcrCalls, ptrCalls
    qcCalls+=1
    #print 'q', start, end
    
    if start < end:
        q, t = Partition(array, start, end)
        #print 'q', q, '\n'
        Quicksort(array, start, q-1)
        #print 'q', start, q, end, '\n'
        Quicksort(array, t+1, end)

def Partition(array, start, end):
    global qcCalls, ptCalls, qcrCalls, ptrCalls
    ptCalls+=1

    copy = array[:]

    #print 'p', start, end
    
    x = array[end]
    i = start-1 # The end of the less than region.
    t = start-1
    for j in range(start, end):
        if array[j] == x:
            t+=1
            array[t], array[j] = array[j], array[t]
        if array[j] < x:
            i+=1
            t+=1
            array[i], array[j] = array[j], array[i]
    array[t+1], array[end] = array[end], array[t+1]
    print copy, start, i+1, t+1, end, array
    return i+1, t


def PartitionRand(array, start, end):
    global qcCalls, ptCalls, qcrCalls, ptrCalls
    ptrCalls+=1
    
    i = random.randint(start, end)
    array[end], array[i] = array[i], array[end]
    return Partition(array, start, end)

def QuicksortRand(array, start, end):
    global qcCalls, ptCalls, qcrCalls, ptrCalls
    qcrCalls+=1

    q = PartitionRand(array, start, end)
    QuicksortRand(array, start, q-1)
    QuicksortRand(array, q+1, end)


alpha = [1,8,3,5,4,7,2,6]
beta = [1,3,2,1,8,3,7,3]
gamma = [2,2,2,2,2,2,2,2]
delta = [7,6,8,5,3,2,4,1]

def stats(array):
    print array
    print "Quicksort & Random calls:", qcCalls, qcrCalls
    print "Partition & Random calls:", ptCalls, ptrCalls

print 'Original array, P value, Q value, T value, R value, New Array'
Quicksort(alpha, 0, 7)
print '\n'
Quicksort(beta, 0, 7)
