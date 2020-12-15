t = int(input())
for T in range(t):
    n, c = [int(x) for x in input().split()]
    l = [0] * n
    for i in range(n):
        l[i] = int(input())
    l.sort()
    lb, ub = 0, l[n - 1]
    mid, ans = 0, 0
    ind = 0
    count, v = 1, 0


    
    while(lb < ub):
        mid = lb + (ub - lb + 1) // 2
        v = 0
        ind = 0
        count = 1
        for i in range(n):
            if l[i] - l[ind] >= mid:
                count += 1
                ind = i
                if count >= c:
                    v = 1
                    break
        if v == 1:
            ans = mid
            lb = mid
        else:
            ub = mid - 1


    print(ans)
