n = int(input())
a = [int(x) for x in input().split()]
c = 0
sum1, sum2 = 0, 0
a.sort(reverse = True)
for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(i + 1):
        sum1 += a[j]
    for j in range(i + 1, n):
        sum2 += a[j]
    if sum1 > sum2:
        c = i + 1
        break
print(c)
