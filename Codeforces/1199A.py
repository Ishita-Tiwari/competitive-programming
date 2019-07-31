n, x, y = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    ans = 0
    for j in range(max(0, i - x), min(i + y + 1, n)):
        if a[i] >= a[j] and i != j:
            ans = -1
    if ans == -1:
        continue
    if ans != -1:
        ans = i + 1
        break
print(ans)
