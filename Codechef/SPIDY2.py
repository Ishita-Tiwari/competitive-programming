n = int(input())
a = [int(x) for x in input().split()]

dp = [-1] * (len(a))
dp[0] = 0

for i in range(n):
    j = 1
    while i + j < len(a):
        print(dp, i, j)
        val = dp[i] + abs(a[i] - a[i + j])
        if dp[i + j] == -1 or dp[i + j] > val:
            dp[i + j] = val
        j *= 2

print(dp[-1])
