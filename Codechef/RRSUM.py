n, m = [int(x) for x in input().split()]

for M in range(m):
    q = int(input())

    if q < n + 2 or q > 3 * n:
        print("0")
        continue
    q -= 1
    val = abs(2 * n - q)
    print(n - val)
