n, k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l.sort()
ans = l[k - 1]
if k < n:
    if l[k] == l[k - 1]:
        ans = -1
if k == 0:
    ans = 1
    if l[0] <= ans:
        ans = -1
print(ans)
