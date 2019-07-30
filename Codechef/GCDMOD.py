def gcd(a, b):
    if a == 0:
        return(b)
    else:
        return(gcd(b % a, a))

t = int(input())
for T in range(t):
    a, b, n = [int(x) for x in input().split()]
    if a == b:
        val1 = pow(a, n, 1000000007) + pow(b, n, 1000000007)
        print(val1 % 1000000007)
    else:
        diff = abs(a - b)
        val1 = (pow(a, n, diff) + pow(b, n, diff)) % diff
        print(gcd(val1, diff) % 1000000007)
    t -= 1
