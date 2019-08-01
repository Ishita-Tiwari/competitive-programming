t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = [0] * (n + 1)
    ans[n - 1] = n * a[n - 1]
    for i in range(n - 2, -1, -1):
        ##print(ans)
        v1 = ans[i + 1] + (i + 1) * a[i]
        v2 = ans[i + 2] + (i + 2) * a[i] + (i + 1) * a[i + 1]
        ans[i] = max(v1, v2)
    print(ans[0])
