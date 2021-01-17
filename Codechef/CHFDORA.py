t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    l = []

    for i in range(n):
        l.append([int(x) for x in input().split()])
    ans = n * m
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            vc = min(j, m - 1 - j)
            vr = min(i, n - 1 - i)
            val = min(vc, vr)

            mnc, mxc = i - val, i + val + 1
            c = []
            for k in range(mnc, mxc):
                c.append(l[k][j])
            
            r = l[i][j - val: j + val + 1]
            
            mid = len(c) // 2
##            if i == mid and j == mid:
##                print(r,c)
            if c == c[::-1] and r == r[::-1]:
                ans += val
            else:
                for k in range(1, val + 1):
    ##                if 
                    if c[mid - k] == c[mid + k] and r[mid - k] == r[mid + k]:
                        ans += 1
                    else:
                        break
    print(ans)
