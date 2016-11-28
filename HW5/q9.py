"""
This module executes the string matching between a input sequence T and an
pattern P using a Finite State Machine.
The complexity for building the transition function is O(m^3 x |A|) where A is the
alphabet. Since the string matching function scan the input sequence only once,
the total complexity is O(n + m^3 x |A|)

@author Filippo Squillace
@version 1.0.0
@date 07/06/2012

http://code.activestate.com/recipes/578161-string-matching-using-a-finit-state-machine/

"""

def Finite_Automaton_Matcher(T, P, m):
    n = len(T)
    q = 0
    for i, c in enumerate(T):
        print P[q][c]
        q = P[q][c]
        print q
        if q == m:
            print "Pattern occurs with shift", i-m
            return i-m
    return -1

def Compute_Transition_Function(P, alphabet):

    m = len(P)
    trans = [{c:0 for c in alphabet} for i in range(m)]
    for q in range(m):
        for a in alphabet:
            k = min(m, q+1)
            Pk = P[:k]
            Pq = (P[:q]+a)[-k:]
            while Pk != Pq:
                k = k-1
                Pk = P[:k]
                Pq = (P[:q] + a)[-k:]
            trans[q][a]=k
    return trans

if __name__=='__main__':

    P = 'aabab'
    T = 'aaababaabaababaab'
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789	')

    trans = Compute_Transition_Function(P, alphabet)
    res = Finite_Automaton_Matcher(T, trans, len(P))
    print 'trans', trans
    print 'res', res
