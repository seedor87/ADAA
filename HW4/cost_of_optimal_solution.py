
x = []
y = []
def solution(i, j):
    opts = []
    try:
        if x[i] == y[j]:
            opts.append(solution(i-1, j-1) + 0)
    except Exception as e:
        pass
    try:
        if x[i] != y[j]:
            opts.append(solution(i-1, j-1) + 1)
    except Exception as e:
        pass
    if (i >= 2 and j >= 2) and (x[i] == y[j-1] or x[i-1] == y[j]):
        opts.append(solution(i-2, j-2) + 1)
    if i == 0:
        opts.append(j)
    if j == 0:
        opts.append(i)
    return min(opts)

x = "Heal"
y = "Heal"

print solution(len(x)-1, len(y)-1)