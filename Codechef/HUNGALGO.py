t = int(input())
for T in range(t):
    n = int(input())
    l = [[]] * n
    L = [[]] * n
    m = 0
    
    for i in range(n):
        l[i] = [int(x) for x in input().split()]
    for i in range(n):
        L[i] = l[i][:]

        
    for i in range(n):
        m = min(l[i])
        for j in range(n):
            l[i][j] -= m

            
    m = l[0][0]
    for i in range(n):
        m = l[0][i]
        for j in range(n):
            if m > l[j][i]:
                m = l[j][i]
        for j in range(n):
            l[j][i] -= m

        
    if l == L:
        print("YES")
    else:
        print("NO")
