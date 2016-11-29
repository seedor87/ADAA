
"""
ANSWER QUESTION 7

To answer the question about the amount of spurious hits, the d value must be given.

To understand the effect of the hashing algorithm being chosen to apply the Rabin-Karp algorithm, the value for d.
d is used for the radix over the interval of which all numbers in the input string, T, exist.

Seen below are several tests conducted on the algorithm across d-radixes of the potential inputs of the test.
The various selections of d (1, 3, 5, 7, 10, 11, 256) yield varying results of spurious hits.

The tests where d = 11 and 7 render accurate runs, with no spurious hits. That is to say, all hits are accurate investigations.

However, when d i snot 7 or 11, the number of spurious hits alters between 1 and 4.

Yet, to answer the assumed question, when d is 10, q is 11, and the given inputs for T, text and P, pattern, are applied,
There are no less than 3 spurious hits. All of which occur before the actual hit is found.


"""
import collections
compare = lambda L1, L2: collections.Counter(L1) == collections.Counter(L2)

def Rabin_Karp_Matcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    total_hits = 0
    successful_hits = 0

    for i in range(m):
        p = ((d * p) + ord(P[i])) % q
        t = ((d * t) + ord(T[i])) % q

    for s in range(n-m+1):
        if p == t:
            print "Hit"
            total_hits += 1
            # check character by character
            if compare(P[1:m], T[(s+1):(s+m)]):
                print "Pattern occurs with shift,", s
                result = result + [s]
                successful_hits +=1
        if s < n-m:
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
    spurious_hits = total_hits - successful_hits
    return result, total_hits, successful_hits, spurious_hits

# print (Rabin_Karp_Matcher(T="xxxxx", P="xx", d=40999999, q=999999937))

print "-" * 50, "d = 1", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=1, q=11))
print "-" * 50, "d = 2", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=2, q=11))
print "-" * 50, "d = 3", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=3, q=11))
print "-" * 50, "d = 5", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=5, q=11))
print "-" * 50, "d = 7", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=7, q=11))
print "-" * 50, "d = 11", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=11, q=11))
print "-" * 50, "d = 256", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=256, q=11))

print "-" * 50, "d = 10", "-" * 50
print "result: %s\ntotal hits: %s\nsuccessful hits: %s\nSPURIOUS HITS: %s" % (Rabin_Karp_Matcher(T="3141592653589793", P="26", d=10, q=11))


# print (Rabin_Karp_Matcher(T="3141592653589793", P="3", d=1, q=11))

