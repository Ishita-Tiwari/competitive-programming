t = int(input())
for T in range(t):
    n = int(input())
    fact = 1
    ans = 0
    for i in range(n):
        fact *= (i + 1)
        ans += fact
    print(ans % 1000000007)
