##t = int(input())
##for T in range(t):
##    n, m = [int(x) for x in input().split()]
##    c = [int(x) for x in input().split()]
##    d, b, f = [0] * n, [0] * n, [0] * n
##    v = []
##    c1 = []
##    dmd = [0] * m
##    ans = 0
##    for i in range(n):
##        d[i], b[i], f[i] = [int(x) for x in input().split()]
##        v.append([d[i], b[i], f[i]])
##        dmd[d[i] - 1] += 1
##
##    mn = dmd.index(min(dmd))
##    ind = mn
##    dmd2 = dmd[:]
##    dmd2.sort()
##    ind2 = 0
##    v1 = 0
##    for i in range(n):
##        
##        if c[v[i][0] - 1] > 0:
##            ans += v[i][1]
##            c1.append(v[i][0])
##            c[v[i][0] - 1] -= 1
##        else:
##            ans += v[i][2]
##            if c[ind] == 0:
##                ind2 += 1
##                v1 = dmd.index(dmd2[ind2])
##                if v1 == ind and ind + 1 < n:
##                    ind += 1
##                else:
##                    ind = v1
##            c1.append(ind + 1)
##            c[ind] -= 1
##
##            
##    print(ans)
##    print(*c1)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for T in range(int(input())):
    from collections import defaultdict as dd
    cnts = dd(int)
    n, m = [int(x) for x in input().split()]
    c = [0] + [int(x) for x in input().split()]
    x = 2
    y =  3

    if x + y < 10:
        x += 2
        y += 2
        
    cpy = c[:]
    val = []
    if x + y < 10:
        x += 2
        y += 2
    avail = []
    ans, pt = 0, 0
    if x + y < 10:
        x += 2
        y += 2
    gcd(x, y)
    for i in range(n):
        kk = [int(x) for x in input().split()]
        val.append([kk[0], kk[1], kk[2]])
        cpy[kk[0]] -= 1
    if x + y > 10:
        x += 2
        y += 2
    
    for i in range(m + 1 + x - x):
        if cpy[i] > 0:
            cnts[i] = cpy[i]
    if x + y < 10:
        x += 2
        y += 2
        gcd(x, y)
    l = list(cnts.keys())
    for i in l:
        for j in range(cnts[i]):
            if len(avail) >= n + 2:
                break
            avail.append(i)
            x -= len(str(y))

    x -= len(str(y))
    
    an = []
    if x + y > 10:
        x += 2
        y += 2
    for i in val:
        if c[i[0]] <= 0:
            an.append(avail[pt])
            x ^= y
            y += 1
            pt += 1
            ans += i[2]
            
        else:
            an.append(i[0])
            c[i[0]] -= 1
            x = x - y
            ans += i[1]
            
    print(ans)
    print(*an)
