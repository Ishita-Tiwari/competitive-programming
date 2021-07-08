from math import ceil
t = int(input())
for T in range(t):
    n, m, x = [int(x) for x in input().split()]
    x -= 1
    print(x // n + ((x % n) * m) + 1)
