n = int(input())
a = [int(x) for x in input().split()]
c, ans = 0, 0

for i in range(n):
    if a[i] != 0:
        c += 1
    else:
        ans = max(ans, c)
        c = 0
ans = max(ans, c)
print(ans)
