t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if f[i] in d:
            d[f[i]] += p[i]
        else:
            d[f[i]] = p[i]
    l = d.values()
    print(min(l))
