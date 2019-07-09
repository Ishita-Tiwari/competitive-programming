n = int(input())
l = [0] * n
for N in range(n):
    a, b = [int(x) for x in input().split()]
    if N == 0:
        l[N] = b
    else:
        l[N] = l[N-1] - a + b
print(max(l))
