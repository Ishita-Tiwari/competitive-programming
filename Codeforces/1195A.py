from math import ceil
 
n, k = [int(x) for x in input().split()]
a = [0] * k
for i in range(n):
    a[int(input()) - 1] += 1
j = 0
ans = 0
for i in a:
    j += i // 2
    ans += i % 2
 
print(n - (ans - (ceil(n / 2) - j)))
