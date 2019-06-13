t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse = True)
    ans = 0
    for i in range(0, n, +2):
        ans += l[i]
    print(ans)
