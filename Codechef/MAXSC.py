t = int(input())
for T in range(t):
    l = []
    n = int(input())
    c = 1
    for i in range(n):
        a = [int(x) for x in input().split()]
        a.sort()
        l.append(a)
    ans = l[n - 1][n - 1]
    ele = ans
    for i in range(len(l) - 2, -1, -1):
        c = 1
        for j in range(n - 1, -1, -1):
            if l[i][j] < ele:
                ele = l[i][j]
                ans += ele
                c = 0
                break
        if c == 1:
            ans = -1
            break
    print(ans)
