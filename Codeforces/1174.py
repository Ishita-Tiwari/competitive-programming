n = int(input())
l = [int(x) for x in input().split()]
l.sort()
s1, s2 = 0, 0
for i in range(n):
    s1 += l[i]
    s2 += l[n + i]
if s1 != s2:
    print(*l)
else:
    print("-1")
