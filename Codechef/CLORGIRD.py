t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    a = []
    c = 0
    for i in range(n):
        a.append(list(input()))
    
    for i in range(n - 1):
        for j in range(m - 1):
            if a[i][j] != '#' and a[i + 1][j] != '#' and a[i][j + 1] != '#' and a[i + 1][j + 1] != '#':
                a[i][j] = 1
                a[i][j + 1] = 1
                a[i + 1][j] = 1
                a[i + 1][j + 1] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] != 1 and a[i][j] != '#':
                c = -1
                break
                
    if c == -1:
        print("NO")
    else:
        print("YES")
