def prod(a, b):
    ans00 = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
    ans01 = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
    ans10 = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
    ans11 = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
    return([ans00, ans01], [ans10, ans11])

def matexpo(a, b):
    n = len(a)
    c = [[1, 0], [0, 1]]

    while(b > 0):
        if b % 2 == 1:
            c = prod(c, a)
        b //= 2
        a = prod(a, a)
    return c

import math
m = 1000000007
for T in range(int(input())):
    l, d, t = [int(x) for x in input().split()]

    cosx = d * pow(l, m - 2, m)
    mt = [[2 * cosx, -1], [1, 0]]
    mt = matexpo(mt, t - 1)

    costx = (mt[0][0] * cosx + mt[0][1]) % m
    print(l * costx % m)
