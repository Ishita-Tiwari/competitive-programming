t = int(input())
for T in range(t):
    a, b, c, r = [int(x) for x in input().split()]
    if a > b:
        a, b = b, a
    total = abs(a - b)
    mn = c - r
    mx = c + r
    if a >= mn:
##        print(1)
        if a <= mx:
            if b <= mx:
                total = 0
            else:
                total -= abs(a - mx)
    elif a <= mn and b >= mx:
##        print(2)
        total -= abs(mn - mx)
    elif b >= mn:
##        print(3)
        total -= abs(b - mn)
        
    total = max(total, 0)
    print(total)
