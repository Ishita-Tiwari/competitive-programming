n, q = [int(x) for x in input().split()]
r = [0] * n
c = [0] * n

for Q in range(q):
    l = [x for x in input().split()]
    ind = int(l[1]) - 1
    inc = int(l[2])
    if l[0] == "RowAdd":
        r[ind] += inc
    else:
        c[ind] += inc
r.sort()
c.sort()
ans = r[-1] + c[-1]
print(ans)
