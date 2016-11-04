
# def solution(i, j):
#     opts = []
#     try:
#         if x[i] == y[j]:
#             opts.append(solution(i-1, j-1) + 0)
#     except Exception as e:
#         pass
#     try:
#         if x[i] != y[j]:
#             opts.append(solution(i-1, j-1) + 1)
#     except Exception as e:
#         pass
#     if (i >= 2 and j >= 2) and (x[i] == y[j-1] or x[i-1] == y[j]):
#         opts.append(solution(i-2, j-2) + 1)
#     if i == 0:
#         opts.append(j)
#     if j == 0:
#         opts.append(i)
#     return min(opts)

def solution(x, y):

    total = 0
    while len(x) > 0 and len(y) > 0:
        at_x, at_y = x.pop(0), y.pop(0)
        if at_x == at_y:
            print "Pass Down\t\t", at_y, 0
            pass
        else:
            if len(x) > 0 and len(y) > 0:
                if x[0] == at_y and at_x == y[0]:
                    print "Twiddle 1\t\t", at_x, 0.5
                    print "Twiddle 2\t\t", at_y, 0.5
                    x.pop(0)
                    y.pop(0)
                    total += 1
            else:
                print "Drop / Add", at_y, "->", at_x, 2
                total += 2
    if len(x) > len(y):
        for char in x:
            print "Insert from X\t", char, 1
            total += 1
    elif len(y) > len(x):
        for char in y:
            print "Delete from Y\t", char, 1
            total += 1
    else:
        pass
    print "\t\t\t Tot:", total

x = "He"
y = "Ha"
solution(list(x), list(y))

x = "Hael"
y = "Heal"
solution(list(x), list(y))

x = "Health"
y = "Heal"
solution(list(x), list(y))