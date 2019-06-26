t = int(input())
for T in range(t):
    a = int(input())
    D1, D2 = 0, 0
    g, r, d = 0, 0, 1

    while(True):
        g += pow(2, (d - 1))
        r = a * d
        if g >= r:
            D1 = d - 1
            break
        d += 1
        
    d = 2
    pr1 = a - 1
    while(True):
        pr2 = (a * d) - pow(2, (d - 1))
        if pr2 > pr1:
            pr1 = pr2
            D2 = d - 1
        else:
            break
        d += 1

    print(D1, D2)
