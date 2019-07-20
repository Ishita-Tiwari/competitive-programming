n, m = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
f.sort(reverse = True)
ans = f[0] - f[n - 1]
val = f[0] - f[n - 1]
for i in range(m - n + 1):
    val = f[i] - f[i + n - 1]
    ans = min(val, ans)
print(ans)
