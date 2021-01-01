n = int(input())
l = []

for N in range(n):
    val = [int(x) for x in input().split()]
    val = val[:-1]
    l.append(val)
l.sort()

for i in range(n):
    print(*l[i])
