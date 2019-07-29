def sm(n):
    ans = 0
    for i in range(1, n + 1, 2):
        x = n // i
        ans += (i * x)
    return ans

t = int(input())
for T in range(t):
    l, r = [int(x) for x in input().split()]
    ans = sm(r) - sm(l - 1)
    print(ans)
