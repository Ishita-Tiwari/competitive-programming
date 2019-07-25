n = int(input())
a = [int(x) for x in input().split()]
a1 = a[:]
p, p1 = 1, 1
 
for i in range(n):
    if a1[i] >= 0:
        a1[i] = -a1[i] - 1
 
if n % 2 == 1:
    ind = a1.index(min(a1))
    a1[ind] = -a1[ind] - 1
 
print(*a1)
