from pprint import pprint
from prettytable import PrettyTable

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

    table = PrettyTable()
    table.field_names = ["Operation:", "at_x:", "at_y:", "Index:", "Total:"]

    if not x or not y:
        return len(x) if len(x) > len(y) else len(y)

    total = 0
    temp = []
    if len(x) > len(y):
        temp = [("Insert", str(x).upper()) for x in x[total:]]
    elif len(y) > len(x):
        temp = [("Delete", str(y).upper()) for y in y[total:]]
    else:
        pass

    zipped = zip(x, y)
    lim = len(zipped)-1
    i = 0
    while i < lim:
        at_x, at_y = str(x[i]).upper(), str(y[i]).upper()
        if at_x == at_y:
            total += 0
            table.add_row(["Copy", str(at_x), str(at_y), str(i), str(total)])
        elif at_x == str(y[i+1]).upper() and at_y == str(x[i+1]).upper():
            total += 1
            table.add_row(["Twiddle 1", str(at_x), str(at_y), str(i), str(total)])
            i += 1
            table.add_row(["Twiddle 2", str(x[i]).upper(), str(y[i]).upper(), str(i), str(total)])
        else:
            total += 2
            table.add_row(["Delete/Insert", str(at_y), str(at_x), str(i), str(total)])
        i += 1
    at_x, at_y = str(zipped[-1][0]).upper(), str(zipped[-1][1]).upper()
    if at_x == at_y:
        total += 0
        table.add_row(["Copy", str(at_x), str(at_y), str(i), str(total)])
    else:
        total += 2
        table.add_row(["Delete/Insert", str(at_y), str(at_x), str(i), str(total)])
    for set in temp:
        total += 2
        table.add_row([set[0], set[1], set[1], str(i), str(total)])
        i += 1
    print table
    return total

x = "We typically apply dynamic programming to"
y = "Dynamic programming typically applies to "
print solution_2(list(x), list(y))


x = ""
y = "Ha"
print solution_2(list(x), list(y))


x = "He"
y = "Ha"
print solution_2(list(x), list(y))


x = "Hael"
y = "Heal"
print solution_2(list(x), list(y))


x = "Health"
y = "Heal"
print solution_2(list(x), list(y))


x = "Help"
y = "Hell"
print solution_2(list(x), list(y))





