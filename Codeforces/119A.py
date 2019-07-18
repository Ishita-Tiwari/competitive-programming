def gcd(a, b):
    if a == 0:
        return(b)
    return(gcd(b%a, a))
 
a, b, n = [int(x) for x in input().split()]
val = 0
i = 1
c = 0
while(n >= 0):
    if i % 2 == 1:
        val = gcd(a, n)
        n -= val
        c = 1
    else:
        val = gcd(b, n)
        n -= val
        c = 0
    i += 1
print(c)
