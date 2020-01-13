n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
b.sort()
ans = m

for i in range(n):
    x = (b[0] - a[i] + m) % m
    for j in range(n):
        if (a[(i + j) % n] + x) % m != b[j]:
            break
    else:
        ans = min(ans, x)
print(ans)
