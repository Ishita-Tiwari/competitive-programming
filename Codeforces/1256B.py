t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    val = [0] * n
    v = 1
    while(v <= n):
        for i in range(n):
##            print(l, v)
            for j in range(n - 1):
##                print(l, v, l[j], l[j + 1], val)
                if l[j] == v:
                    if val[j] == 0:
                        if l[j] > l[j + 1]:
                            l[j + 1], l[j] = l[j], l[j + 1]
                            val[j] = 1
                elif l[j + 1] == v:
                    if val[j + 1] == 0:
                        if l[j] > l[j + 1]:
                            l[j + 1], l[j] = l[j], l[j + 1]
                            val[j + 1] = 1
            if l[n - 1] == v:
                if val[n - 1] == 0:
                    if l[n - 2] > l[n - 1]:
                        l[n - 2], l[n - 1] = l[n - 1], l[n - 2]
                
        else:
            v += 1
    print(*l)
