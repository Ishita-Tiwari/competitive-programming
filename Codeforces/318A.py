n, k = [int(x) for x in input().split()]
num = 2 * (k - ((n + 1) // 2))
if num > 0:
    print(num)
else:
    print((2 * k) - 1)
