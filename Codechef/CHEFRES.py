t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    l, r = [0] * n, [0] * n
    val = []
    for i in range(n):
        l[i], r[i] = [int(x) for x in input().split()]
        val.append([l[i], r[i]])
    val.sort()
    for i in range(n):
        l[i], r[i] = val[i][0], val[i][1]

    for i in range(m):
        p = int(input())
        lb, ub, ind, ans, c = 0, n - 1, 0, 0, 0
        if p < r[0]:
            print(max(l[0] - p, 0))
        elif p >= r[n - 1]:
            print("-1")
        else:
            while(lb <= ub):
                mid = (lb + ub) // 2
                
                if p > r[mid]:
                    if mid != n - 1:
                        if p < r[mid + 1]:
                            ans = max(l[mid + 1] - p, 0)
                            print(ans)
                            c = 1
                            break
                        else:
                            lb = mid + 1
                    else:
                        print("-1")
                        c = 1
                        break
                elif p == r[mid]:
                    ans = max(l[mid + 1] - p, 0)
                    print(ans)
                    c = 1
                    break
                else:
                    ub = mid - 1
            if c != 1:
                print(ans)
