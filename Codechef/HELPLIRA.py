n = int(input())
area = []
mn, mx = 0, 0
indmn, indmx = 1, 1
for N in range(n):
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
    val = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    val /= 2
    val = abs(val)
    area.append(val)
    if N == 0:
        mn, mx = val, val
    else:
        if val <= mn:
            mn = val
            indmn = N + 1
        if val >= mx:
            mx = val
            indmx = N + 1

print(indmn, indmx)
