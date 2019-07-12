c = 0
n = int(input())
for N in range(n):
    p, q = [int(x) for x in input().split()]
    if q - p >= 2:
        c += 1
print(c)
