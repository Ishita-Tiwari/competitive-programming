t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    
    for i in range(n - 1):
        mn = min(a[i], a[i + 1])
        mx = max(a[i], a[i + 1])

        if 2 * mn >= mx:
            continue
        else:
            while True:
                
                if 2 * mn >= mx:
                    break
                mn = mn * 2
                ans += 1
    print(ans)
