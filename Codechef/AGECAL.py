t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    yb, mb, db = [int(x) for x in input().split()]
    yc, mc, dc, = [int(x) for x in input().split()]
    mb -= 1
    mc -= 1
    ans = 0
    if yb == yc:
        if mb == mc:
            print(dc - db + 1)
        else:
            ans += (a[mb] - db)
            for i in range(mb + 1, mc):
                ans += a[i]
            ans += dc
            print(ans + 1)
    else:
        ans, leap = 0, 0
        ans += (a[mb] - db)
        mb += 1
        for i in range(mb, n):
                ans += a[i]
        if yb % 4 == 0:
            leap = 1
        yb += 1
        tt = sum(a)
        while(yc != yb):
            ans += tt
            if yb % 4 == 0 and yb <= yc - 1:
                leap += 1
            yb += 1
        if yb == yc:
            for i in range(mc):
                ans += a[i]
            ans += dc
        ans += leap
        print(ans + 1)
