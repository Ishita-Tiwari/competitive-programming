t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    d, v = [0] * n, [0] * n
    v1= [0] * n
    for i in range(n):
        d[i], v[i] = [int(x) for x in input().split()]
    v1 = v[:]
    v1.sort(reverse = True)
    val1 = v1[0]
    d1 = d[v.index(val1)]
##    print(val1, d1)
    l = [[]]
    for i in range(n):
        l.append([v[i], d[i]])
    l.sort()
    val1 = l[n][0]
    d1= l[n][1]
    d2 = 0
    
    for i in range(n - 1, -1, -1):
        if l[i][1] != d1:
            d2 = i
            break
    val2 = l[d2][0]
##    print(val1, val2)
    print(val1 + val2)
