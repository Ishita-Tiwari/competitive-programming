t = int(input())
mod = 10**9 + 7
for T in range(t):
    n, a = [int(x) for x in input().split()]
    curr = a
    multiplier = 1
    rest = a
    ans = 0
    
    for i in range(1, n + 1):
        curr = pow(curr, multiplier, mod)
        rest = (curr % mod * rest % mod) % mod
        ans = (ans % mod + curr) % mod
        curr = rest
        multiplier += 2
    print(ans)
