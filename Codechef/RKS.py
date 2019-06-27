t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    p, j = n - k, 1
    ans = [0] * (2 * p + 1)
    ans[0] = p
    r = [0] * k
    c = [0] * k
    for i in range(k):
        r[i], c[i] = [int(x) for x in input().split()]
    r1 = set(r)
    c1 = set(c)
    for i in range(1, n + 1):
        if j > 2 * p - 1:
            break
        if i not in r1:
            ans[j] = i
            j += 2
    j = 2
    
    for i in range(1, n + 1):
        if j > 2 * p:
            break
        if i not in c1:
            ans[j] = i
            j += 2

    print(*ans)
