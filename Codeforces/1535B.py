from math import gcd

t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    mul2, rest = [], []
    for i in l:
        if i % 2 == 0:
            mul2.append(i)
        else:
            rest.append(i)

    rest.sort(reverse = True)
    fnl = mul2 + rest
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(fnl[i], 2 * fnl[j]) > 1:
                ans += 1
    
    print(ans)
