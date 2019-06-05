def gcd(a, b):
    if a == 0:
        return b
    return(gcd(b % a, a))

t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    n = l[0]
    val = l[1]
    for i in range(1, n+1):
        val = gcd(val, l[i])
    for i in range(1, n+1):
        l[i] = l[i] // val
        print(l[i], end=" ")
    print()
