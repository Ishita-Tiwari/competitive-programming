t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = -1

    for i in range(1, n - 1):
        if a[i] - a[i - 1] != 1 or a[i + 1] - a[i] != 1:
            ans = a[i]
    if a[1] - a[0] != 1:
        ans = a[0]
    if a[n - 1] - a[n - 2] != 1:
        ans = a[n - 1]

    print(ans)
