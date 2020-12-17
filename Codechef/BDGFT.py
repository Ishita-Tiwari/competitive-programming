for t in range(int(input())):
    s = list(input())
    s = [int(i) for i in s]
    
    n = len(s)
    dp = [0 for i in range(n + 1)]
    for i in range(n):
        dp[i + 1] = dp[i] + s[i]
    l = 1
    ans = 0
    while l <= (n ** 0.5):
        ln = (l ** 2) + l
        
        for i in range(n - ln + 1):
            x = dp[i + ln] - dp[i]
            y = ln - x
            if y == x ** 2:
                ans += 1
        l += 1
    print(ans)
