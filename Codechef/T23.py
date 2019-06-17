def gcd(a, b):
    if a == 0:
        return(b)
    else:
        return(gcd(b % a, a))
    
t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    c = 0
    a.sort()
    if a[0] == 1:
        print("YES")
        continue
    for i in range(n - 1):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) == 1:
                c = 1
                break
    if c == 1:
        print("YES")
    else:
        print("NO")
