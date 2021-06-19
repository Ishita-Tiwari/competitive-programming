t = int(input())
for T in range(t):
    l = []
    for i in range(9):
        l.append(list(input()))
    for i in range(9):
        for j in range(9):
            l[i][j] = int(l[i][j])

    
    l[0][0] += 1
    l[1][4] += 1
    l[2][8] += 1
    l[3][1] += 1
    l[4][5] += 1
    l[5][6] += 1
    l[6][2] += 1
    l[7][3] += 1
    l[8][7] += 1
    
    
    for i in range(9):
        for j in range(9):
            if l[i][j] == 10:
                l[i][j] = 1
            l[i][j] = str(l[i][j])

    for i in range(9):
        row = ''.join(l[i])
        print(row)
