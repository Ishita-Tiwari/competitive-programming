t = int(input())
for T in range(t):
    n = int(input())
    if n == 2:
        print(-1)
        continue
    l = [[0 for i in range(n)] for j in range(n)]
    val = [n**2]
    for i in range(2, n**2):
        val.append(i)
    val.append(1)


    # filling the necessary matrix
    l[0][0] = val[0]
    ind = 1
    for i in range(1, n):
        j = 0
        col = i
        while(col >= 0):
            l[j][col] = val[ind]
            col -= 1
            j += 1
            ind += 1
    for i in range(1, n):
        j = n - 1
        row = i
        while(j >= 0 and row < n):
            l[row][j] = val[ind]
            j -= 1
            row += 1
            ind += 1
            
    for i in range(n):
        print(*l[i])
