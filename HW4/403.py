strx = "algorithm"
stry = "altruistic"

para1 = """This part covers three important techniques used in designing and analyzing effi-
cient algorithms:  dynamic programming (Chapter 15), greedy algorithms (Chap-
ter 16),  and amortized analysis  (Chapter 17).  Earlier parts have presented  other
widely applicable techniques, such as divide-and-conquer, randomization, and how
to solve recurrences. The techniques in this part are somewhat more sophisticated,
but they help us to attack many computational problems. The themes introduced in
this part will recur later in this book."""
para2 = """Dynamic programming typically applies to optimization problems in which we
make  a  set  of  choices  in  order  to  arrive  at  an  optimal  solution.   As  we  make
each choice,  subproblems  of the same form often arise.  Dynamic programming
is effective when a given subproblem may arise from more than one partial set of
choices; the key technique is to store the solution to each such subproblem in case it
should reappear. Chapter 15 shows how this simple idea can sometimes transform
exponential-time algorithms into polynomial-time algorithms."""

def cost(x,y):
    #x = ''.join(x.split())
    #y = ''.join(y.split())
    m = len(x)
    n = len(y)
    c = [[0 for xx in range(0,n)] for yy in range(0,m)]
    b = [[0 for xx in range(0,n)] for yy in range(0,m)] 
    out = x

    for i in range(0,m):
        for j in range(0,n):
            if i > 1 and j > 1 and x[i] == y[j-1] and x[i-1] == y[j]: # Twiddle
                c[i][j] = c[i-2][j-2] + 1
                b[i][j] = 'T'
                #out = y[j-1] + x[i] + out
            elif i != j:
                if m > n:
                    c[i][j] = c[i-1][j] + 1
                    b[i][j] = "D"
                else:
                    c[i][j] = c[i][j-1] + 1
                    b[i][j] = "I"
            elif x[i] == y[j]: # Copy
                c[i][j] = c[i-1][j-1]+0
                b[i][j] = 'C'
            elif x[i] != y[j]: # Toss 
                c[i][j] = c[i-1][j-1]+1
                #out = y[i] + out
                b[i][j] = 'R'
                
    return c[i][j], b
def prints(b, i, j):
    #print i, j
    if i < 0 or j < 0:
        return None
    if b[i][j] == 'T':
        prints(b,i-2,j-2)
        print 'Twiddle'
    elif b[i][j] == "I":
        prints(b,i,j-1)
        print 'Insert'
    elif b[i][j] == "D":
        prints(b,i-1,j)
        print 'Delete'
    elif b[i][j] == 'C':
        prints(b,i-1,j-1)
        print 'Copy'
    elif b[i][j] == 'R':
        prints(b,i-1,j-1)
        print 'Replace'

test1 = cost('hello', 'hleoe')
test2 = cost(strx, stry)
test3 = cost(para1, para2)
print test3[0]
#prints(test1[1],4,4)
#prints(test2[1],len(strx)-1,len(stry)-1)
prints(test3[1],len(para1)-1,len(para2)-1)
