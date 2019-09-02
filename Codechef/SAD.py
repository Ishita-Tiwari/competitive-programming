r, c = [int(x) for x in input().split()]
ans, v, ind = -1, 0, 0
row, col1 = [], [[0] * r] * c
col = []
val = [[0] * c]
for i in range(r):
    row.append([int(x) for x in input().split()])
for i in range(c):
    for j in range(r):
        col1[i][j] = row[j][i]
    col.append(col1[i][:])
for i in range(r):
    v = min(row[i])
    for j in range(c):
        if row[i][j] == v:
            ind = j
            if max(col[ind]) == v:
                ans = v
if ans != -1:
    print(ans)
else:
    print("GUESS")
