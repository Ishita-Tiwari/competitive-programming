t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ans = 0
    profit = 0
    for i in range(n):
        profit = (k // a[i]) * b[i]
        ans = max(ans, profit)
    print(ans)
