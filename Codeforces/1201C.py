n, k = [int(x)for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
ind, val = n // 2, 0
ans, ind1 =  a[ind], 1

for i in range(ind + 1, n):
    val = (a[i] - a[i - 1]) * ind1
    if k - val >= 0:
        k -= val
        ind1 += 1
        ans = a[i]
    else:
        ans = a[i - 1] + (k // ind1)
        k = 0
        break
if k != 0:
    ans += k // ind1
print(ans)
