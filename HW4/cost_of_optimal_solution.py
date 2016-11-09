
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' %(highlight, text, color.END)

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
    result = []
    while len(x) > 0 and len(y) > 0:
        at_x, at_y = x.pop(0), y.pop(0)
        if at_x == at_y:
            print "Copy \t\t", wrap_text(str(0), color.GREEN), wrap_text(str(at_y), color.CYAN), wrap_text(str("Y: " + str(y)), color.PURPLE)
            result.append(at_y)
            pass
        elif len(x) > 0 and len(y) > 0:
            if x[0] == at_y and at_x == y[0]:
                print "Twiddle\t\t\t", wrap_text(str(1), color.YELLOW), wrap_text(str(at_y), color.CYAN), wrap_text(str("Y: " + str(y)), color.PURPLE)
                result.append(y.pop(0))
                result.append(x.pop(0))
                total += 1
        else:
            print "Drop / Add", wrap_text(str(at_y) + ' -> ' + str(at_x), color.CYAN), wrap_text(str(2), color.RED), wrap_text(str("Y: " + str(y)), color.PURPLE)
            result.append(at_x)
            total += 2
    if len(x) > len(y):
        while len(x) > 0:
            at_x = x.pop(0)
            print "Insert from X\t", wrap_text(str(1), color.YELLOW), wrap_text(str(at_x), color.CYAN), wrap_text(str("Y: " + str(y)), color.PURPLE)
            result.append(at_x)
            total += 1
    elif len(y) > len(x):
        while len(y) > 0:
            at_y = y.pop(0)
            print "Delete from Y\t", wrap_text(str(1), color.YELLOW), wrap_text(str(at_y), color.CYAN), wrap_text(str("Y: " + str(y)), color.PURPLE)
            total += 1
    else:
        pass
    print "\t\t\t Tot:", total
    print '\t\t\t Result:', ''.join(result)

def solution_2(x, y):

    if not x or not y:
        return len(x) if len(x) > len(y) else len(y)

    total = 0
    if len(x) > len(y):
        total += len(x)-len(y)
    else:
        total += len(y)-len(x)

    zipped = zip(x, y)
    lim = len(zipped)-1
    i = 0
    while i < lim:
        at_x, at_y = x[i], y[i]
        if at_x == at_y:
            total += 0
        elif at_x == y[i+1] and at_y == x[i+1]:
            i += 1
            total += 1
        else:
            total += 2
        i += 1
    at_x, at_y = zipped[-1]
    if at_x == at_y:
        total += 0
    else:
        total += 2
    return total

x = "We typically apply dynamic programming t"
y = "Dynamic programming typically applies to"
solution(list(x), list(y))
print solution_2(list(x), list(y))

x = ""
y = "Ha"
solution(list(x), list(y))
print solution_2(list(x), list(y))


x = "He"
y = "Ha"
solution(list(x), list(y))
print solution_2(list(x), list(y))


x = "Hael"
y = "Heal"
solution(list(x), list(y))
print solution_2(list(x), list(y))


x = "Health"
y = "Heal"
solution(list(x), list(y))
print solution_2(list(x), list(y))


x = "Help"
y = "Hell"
solution(list(x), list(y))
print solution_2(list(x), list(y))





