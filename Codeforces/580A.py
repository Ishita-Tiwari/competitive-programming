n = int(input())
a = [int(x) for x in input().split()]
c = 1
l = [1] * n
j = 0
for i in range(1, n):
    if a[i] >= a[i - 1]:
        c += 1
    l[j] = c
    if a[i] < a[i - 1]:
        c = 1
        j += 1
print(max(l))
