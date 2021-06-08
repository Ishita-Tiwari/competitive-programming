n, m, a, b = [int(x) for x in input().split()]
if a < b / m:
    print(n * a)
else:
    countM = n // m
    total = (n - countM * m) * a + countM * b
    countM += 1
    countM *= b
    print(min(total, countM))
