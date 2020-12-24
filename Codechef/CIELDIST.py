t = int(input())
for T in range(t):
    ds, dt, d = [int(x) for x in input().split()]

    
    ans = 0
    ans = max(ans, d - (ds + dt))
    ans = max(ans, ds - (d + dt))
    ans = max(ans, dt - (d + ds))

    
    print(ans)
