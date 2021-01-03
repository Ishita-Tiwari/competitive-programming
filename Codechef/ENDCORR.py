n, m = [int(x) for x in input().split()]
a = []

for i in range(n + m):
    val = int(input())
    if val == -1:
        print(a.pop())
    else:
        if len(a) < m:
            a.append(val)
            a.sort()
        elif len(a) == m and val > a[0]:
            a[0] = val
            a.sort()
