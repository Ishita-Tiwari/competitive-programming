k, n, w = [int(x) for x in input().split()]
cost = ((w * (w + 1)) // 2) * k
if cost > n:
    print(cost - n)
else:
    print(0)
