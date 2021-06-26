t = int(input())
for T in range(t):
    n = int(input())
    stats = []
    ans = 'YES'
    for i in range(n):
        stats.append([int(x) for x in input().split()])
        if stats[i][0] < stats[i][1]:
            ans = 'NO'
    
    for i in range(1, n):
        d1 = stats[i][0] - stats[i - 1][0]
        d2 = stats[i][1] - stats[i - 1][1]
        if d1 < 0 or d2 < 0 or d1 < d2:
            ans = 'NO'
        
    print(ans)
