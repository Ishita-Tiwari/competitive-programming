t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    if l[0] == 0:
        ans = 1
    for i in range(1, n):
        if l[i] <= ans:
            ans += 1
    print(ans)
