n = int(input())
l = [int(x) for x in input().split()]

l.sort()
st = set(l)
mxdiff = l[-1] - l[0]
ans = 0
count = dict()
for i in range(n):
    if l[i] not in count:
        count[l[i]] = 1
    else:
        count[l[i]] += 1
for i in st:
    if i + mxdiff in count:
        ans += count[i] * count[i + mxdiff]
if mxdiff == 0:
    ans = n * (n - 1) // 2
print(mxdiff, ans)
