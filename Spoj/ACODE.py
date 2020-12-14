s = input()
while(s != '0'):
    s = list(s)
    l = len(s)
    dp = [0] * l
    dp[0] = 1
    for i in range(l):
        s[i] = int(s[i])

    if l > 1 and s[1] == 0:
        dp[0] = 0
        
    for i in range(1, l):
        if s[i] != 0:
            dp[i] = dp[i - 1]
        num = s[i - 1] * 10 + s[i]
        if num > 9 and num <= 26:
            if i == 1:
                if dp[0] == 0:
                    dp[i] = 1
                else:
                    dp[1] = 2
            else:
                dp[i] += dp[i - 2]

    print(dp[l - 1])
    s = input()
