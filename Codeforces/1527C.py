t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    d = dict()
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    cur = 0
    ans = 0
    for i in d:
        cur = d[i][0] + 1
        for j in range(1, len(d[i])):
            ans += (n - d[i][j]) * cur
##            print(d[i], i, ans, cur)
##            print(cur)
            cur += d[i][j] + 1

    print(ans)
