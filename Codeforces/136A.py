n = int(input())
a = [int(x) for x in input().split()]
a1 = [0] * n
for i in range(n):
    a[i] -= 1
for i in range(n):
    a1[i] = a.index(i) + 1
print(*a1)
