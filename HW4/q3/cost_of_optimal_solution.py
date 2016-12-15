from prettytable import PrettyTable

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

    table = PrettyTable()
    table.field_names = ["Operation:", "   at_x:   ", "   at_y:   ", "Index:", "Unit Increase:", "Total:"]

    total = 0
    zipped = zip(x, y)
    lim = len(zipped) - 1
    i = 0
    if not x or not y:
        pass
    else:
        while i < lim:
            at_x, at_y = str(x[i]).upper(), str(y[i]).upper()
            if at_x == at_y:
                total += 0
                table.add_row(["Copy", str(at_x), str(at_y), str(i), "+= 0", str(total)])
            elif at_x == str(y[i+1]).upper() and at_y == str(x[i+1]).upper():
                table.add_row(["Twiddle 1", str(at_x), str(at_y), str(i), "+= 1/2" ,str(total)])
                total += 1
                i += 1
                table.add_row(["Twiddle 2", str(x[i]).upper(), str(y[i]).upper(), str(i), "+= 1/2", str(total)])
            else:
                total += 2
                table.add_row(["Delete/Insert", str(at_y), str(at_x), str(i), "+= 2", str(total)])
            i += 1
        at_x, at_y = str(zipped[-1][0]).upper(), str(zipped[-1][1]).upper()
        if at_x == at_y:
            total += 0
            table.add_row(["Copy", str(at_x), str(at_y), str(i), "+= 0", str(total)])
        else:
            total += 2
            table.add_row(["Delete/Insert", str(at_y), str(at_x), str(i), "+= 2", str(total)])
        i += 1

    if len(x) > len(y):
        while i < len(x):
            at_x = str(x[i]).upper()
            total += 1
            table.add_row(["Insert from X", ' ', str(at_x), str(i), "+= 1", str(total)])
            i += 1
    elif len(y) > len(x):
        while i < len(y):
            at_y =str(y[i]).upper()
            total += 1
            table.add_row(["Delete from Y", str(at_y), ' ', str(i), "+= 1", str(total)])
            i += 1
    else:
        pass

    print table
    return total


x = "HA"
y = ""
print solution(list(x), list(y))


x = "He"
y = "Ha"
print solution(list(x), list(y))


x = "Hael"
y = "Heal"
print solution(list(x), list(y))


x = "Health"
y = "Heal"
print solution(list(x), list(y))


x = "Help"
y = "Hell"
print solution(list(x), list(y))


x = 'Winner'
y = 'looser'
print solution(list(x), list(y))


x = 'altruistic'
y = 'algorithm'
print solution(list(x), list(y))


x = "We typically apply dynamic programming to"
y = "Dynamic programming typically applies to "
print solution(list(x), list(y))

para1 = """This part covers three important techniques used in designing and analyzing effic"""
para2 = """Dynamic programming typically applies to optimization problems in which we make a"""
print solution(list(para1), list(para2))





