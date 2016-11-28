"""
Code exhibited at source,

http://code.activestate.com/recipes/578161-string-matching-using-a-finit-state-machine/
"""

def Finite_Automaton_Matcher(T, trans, m):
    q = 0
    for i, c in enumerate(T):
        q = trans[q][c]
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
    # alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789	')
    alphabet = list('ab')
    trans = Compute_Transition_Function(P, alphabet)
    print 'trans', trans
    res = Finite_Automaton_Matcher(T, trans, len(P))
    print 'res', res

"""
By tracing the preceding code we will find the operation of the string automaton and learn the way in which it operates.

First we begin wth the usage of the Compute Transition Function to generate the object trans. Trans is a collection object that allows us to store the references to the counts of local occurrences in the input string

The result of running the method on the pattern 'aabab' on the alphabet 'ab' is...
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 4, 'b': -5}, {'a': 2, 'b': 5}]

By leveraging the python dictionary class, we can dynamically store the location of each of the encountered occurrences of each letter in the alphabet as we process the input text.

After the first iteration, the trans object is,
[{'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]

Following this iteration, the next incarnation of trans will be,
[{'a': 1, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]
This is the case as we have found only one 'a' while parsing through the pattern, P, to index 1

Following this iteration the next will be,
[{'a': 1, 'b': -5}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]
This is the case as we have found not one, but two 'a's up until the index 2 of the pattern

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 0}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]
this is the case as we have yet to reach teh first b at index 3

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 0, 'b': 0}, {'a': 0, 'b': 0}]
This is the case as we have finally reached an incident of b, so we store it with its first encountered index, 3

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 4, 'b': 0}, {'a': 0, 'b': 0}]

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 4, 'b': -5}, {'a': 0, 'b': 0}]

Next,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 4, 'b': -5}, {'a': 0, 'b': 0}]

Finally,
[{'a': 1, 'b': -5}, {'a': 2, 'b': -5}, {'a': 2, 'b': 3}, {'a': 4, 'b': -5}, {'a': 2, 'b': 0}]

This collection of dictionaries is used to follow the enumerated input string, in the call to the Finite Automaton Matcher.
The enumerated input string is the list of tuples of each letter in the input string tied to the index of that letter in the input string.

Using these values we can retrace the trans object, the collection of dictionaries storing states of the pattern on parsing, and collectively choose a match wherein the pattern lies.

The loop accomplishing the work of unrolling the trans dictionaries is accomplished in the block...

for i, c in enumerate(T):
        q = trans[q][c]
        if q == m:
            print "Pattern occurs with shift", i-m
            return i-m

this loop will run over each element indexed by i and determine the match in input text when the max value is reached.

First iteration,
c = 'a', i = 0
q = 0

Next iteration,
c = 'a', i = 1
q = 1

Next,
c = 'a', i = 2
q = 2

Next,
c = 'b', i = 3
q = 2

Next,
c = 'a', i = 4
q = 3

Final,
c = 'b', i = 5
q = 4

the returned result is 4, this is the final value of q as well as i - m, the final index of the pattern P minus the length of P
"""
