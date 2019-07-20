l = [[]] * 5
r, c = 0, 0
for i in range(5):
    l[i] = [int(x) for x in input().split()]
    if 1 in l[i]:
        r = i
        c = l[i].index(1)
ans = abs(2 - r) + abs(2 - c)
print(ans)
