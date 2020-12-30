def calc(n, k, a):
    v1, v2 = 0, 0
    for i in range(k):
        v1 = a[i % n]
        v2 = a[n - (i % n) - 1]
        a[i % n] = v1 ^ v2

    return(a)

t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    
    if k <= 3 * n + 1:
        ans = calc(n, k, a)
    else:
        ans = calc(n, k % (3 * n), a)
        if n % 2 == 1:
            ans[n // 2] = 0
    print(ans)
