t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    diff = []
    cor = 0
    
    for i in range(1, n):
        diff.append(a[i] - a[i - 1])
    d = set(diff)
    d = list(d)
    
    if len(d) == 1:
        print(*a)
        continue
    if len(d) == 2:
        cor = a[2] - a[1]
        if a[1] - a[0] != cor:
            a[0] = a[1] - cor
        else:
            a[-1] = a[-2] + cor
        print(*a)
        continue

    
    if (d[0] + d[1]) / 2 == d[2]:
        cor = d[2]
    elif (d[1] + d[2]) / 2 == d[0]:
        cor = d[0]
    else:
        cor = d[1]
    for i in range(1, n):
        if a[i] - a[i - 1] != cor:
            a[i] = a[i - 1] + cor
    print(*a)
