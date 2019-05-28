def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a , a)

t = int(input())
while(t > 0):
    n, m, k = [int(x) for x in input().split()]
    valN = gcd(n, k)
    valM = gcd(m, k)
    if valN == 1 and valM == 1:
        print(n * m)
    else:
        print(-1)
    t -= 1
