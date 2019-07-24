n = int(input())
a = [int(x) for x in input().split()]
d = [0] * n
ans = 0
for i in range(n):
    d[i] = a[i] % 2
for i in range(2, n):
    if d[i] != d[i - 1] and d[i] != d[i - 2]:
        ans = i
    elif d[i - 1] != d[i] and d[i - 1] != d[i - 2]:
        ans = i - 1
    elif d[i - 2] != d[i] and d[i - 2] != d[i - 1]:
        ans = i - 2
print(ans + 1)
