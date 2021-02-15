t = int(input())
for T in range(t):
##    n = int(input())
##    a = [int(x) for x in input().split()]
##    a.sort()
##    v1, v2, v3 = a[0], a[1], a[-1]
##    ans = v2 - v1 + v3 - v1 + v3 - v2
##
##    for i in range(1, n - 1):
##        val = a[i] - v1 + v3 - v1 + v3 - a[i]
##        ans = max(ans, val)
####        print(i, a[i], ans)
##    print(ans)

    n = int(input())
    a = [int(x) for x in input().split()]
    print(2 * max(a) - 2 * min(a))
