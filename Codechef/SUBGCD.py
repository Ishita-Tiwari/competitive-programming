def gcd(a, b):
    if a == 0:
        return b
    return(gcd(b % a, a))

t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    g1 = a[0]
    val = 0
    
    for i in range(1, n):
        if gcd(g1, a[i]) == 1:
            val += 1
    if val > 0:
        print(n)
    else:
        print("-1")
