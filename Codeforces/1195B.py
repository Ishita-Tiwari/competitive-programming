n, k = [int(x) for x in input().split()]
d = (8 * (k + n)) + 9
ans = (d ** 0.5) - 3
ans //= 2
ans = n - ans
print(int(ans))
