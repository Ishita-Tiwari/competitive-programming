def binexpo(a, b, m):
    a %= m
    res = 1
    while(b > 0):
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return(res)

t = int(input())
for T in range(t):
    k = int(input())
    ans = (binexpo(2, (k - 1), 1000000007) * 10) % 1000000007
    print(ans)
