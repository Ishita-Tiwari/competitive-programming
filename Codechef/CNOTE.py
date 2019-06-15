t = int(input())
for T in range(t):
    x, y, k, n = [int(x) for x in input().split()]
    p = [0] * n
    c = [0] * n
    for i in range(n):
        p[i], c[i] = [int(x) for x in input().split()]
    pages = x - y
    count = 0
    for i in range(n):
        if p[i] >= pages and c[i] <= k:
            count = 1
    if count == 1:
        print("LuckyChef")
    else:
        print("UnluckyChef")
