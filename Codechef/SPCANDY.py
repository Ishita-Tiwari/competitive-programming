t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    if k == 0:
        print("0", n)
    else:
        print((n // k), (n % k))
