dp = {}
def cal(n):
    if n not in dp:
        dp[n] = max(n, cal(n // 2) + cal(n // 3) + cal(n // 4))
    return(dp[n])

for i in range(12):
    dp[i] = i
            
while(True):
    try:
        n = int(input())
        print(cal(n))
    except:
        break
