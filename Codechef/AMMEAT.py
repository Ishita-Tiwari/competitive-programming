t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse = True)
    for i in range(1, n):
        a[i] += a[i - 1]
    ans = -1
    for i in range(n):
        if a[i] >= m:
            ans = i + 1
            break
    print(ans)
