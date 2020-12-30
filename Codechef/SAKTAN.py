t = int(input())
for T in range(t):
    n, m, q = [int(x) for x in input().split()]
    r = [0] * n
    c = [0] * m
    ans = 0
    oddr, evec = 0, 0
    
    for Q in range(q):
        x, y = [int(x) for x in input().split()]
        r[x - 1] += 1
        c[y - 1] += 1
    for i in range(n):
        if r[i] % 2 == 1:
            oddr += 1
    for i in range(m):
        if c[i] % 2 == 0:
            evec += 1

    ans = (oddr * evec) + ((n - oddr) * (m - evec))
    
    print(ans)
