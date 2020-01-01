t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    ans = 0
    l.sort()

    mini = l[0]
    l[0] -= min(l[0], l[2] - l[1])
    l[1] += min(mini, l[2] - l[1])
    ans = min(l[1], l[2])
    ans += l[0] // 2
    print(ans)
