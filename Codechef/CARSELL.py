t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse = True)
    ans = 0
    for i in range(n):
        ans += max(l[i] - i, 0)
    print(ans % 1000000007)
