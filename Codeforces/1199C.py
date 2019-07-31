n, I = [int(x) for x in input().split()]
d = pow(2, (8 * I // n))
a = [int(x) for x in input().split()]
a.sort()
val = [0]
m = 0
for i in range(1, n):
    if a[i - 1] != a[i]:
        val.append(i)
        
diff = len(val) - d
if len(val) <= d:
    print("0")
else:
    for i in range(diff):
        m = max(val[i + d] - val[i], m)
    print(n - m)
