t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    cost, disc, dp = [], [], []
    for i in range(n):
        cost.append([int(x) for x in input().split()])
    for i in range(n):
        disc.append([int(x) for x in input().split()])
    
    val = 0
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):
        dp[0][i] = cost[0][i]
##        print(dp)
    for i in range(1, n):
        val = min(dp[i - 1])
        for j in range(m):
            v1 = max(0, cost[i][j] - disc[i - 1][j])
            dp[i][j] = min(dp[i - 1][j] + v1, val + cost[i][j])
##            print(dp)
    print(min(dp[n - 1]))
