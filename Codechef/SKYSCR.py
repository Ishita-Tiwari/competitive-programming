t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    if n < m:
        m, n = n, m
    print(n - m)
