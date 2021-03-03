t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    a.sort()
    mn = a[0]
    ans = n - a.count(mn)
    print(ans)
