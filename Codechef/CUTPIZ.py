def gcd(a, b):
    if a == 0:
        return b
    return(gcd(b % a, a))

t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]

    ang = []
    for i in range(1, n):
        ang.append(l[i] - l[i - 1])
    ang.append(360 - (l[-1] - l[0]))
    ang.sort()
    if ang == ang[::-1]:
        print(0)
        continue
    
    g = ang[0]
    for i in range(1, n):
        g = gcd(g, ang[i])

    
    total = 360 // g - len(ang)
    print(total)

