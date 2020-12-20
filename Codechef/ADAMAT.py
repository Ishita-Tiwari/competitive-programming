t = int(input())
for T in range(t):
    n = int(input())
    cor = [i for i in range(1, n + 1)]
    l = []
    val = []
    c = 0
    fin = []

    for i in range(n):
        l.append([int(x) for x in input().split()])
    a = l[0][:]

    if a == cor:
        print(0)
        continue

    for i in range(1, n):
        if a[i] == cor[i]:
            val.append(1)
        else:
            val.append(-1)

    fin.append(val[0])
    for i in range(1, len(val)):
        if val[i] != fin[-1]:
            fin.append(val[i])
    
    if len(fin) > 0:
        if fin[-1] == 1:
            del fin[-1]

    print(len(fin))
