t = int(input())
for T in range(t):
    n, p, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort()
    l1 = [0]

    for i in range(k - 1):
##        print(l1)
        l1.append(l1[-1] + l[i])
    for i in range(k - 1, n):
##        print(l1)
        l1.append(l1[i - k + 1] + l[i])
##    print(l1)
    ind = 0
    while(ind <= n):
        if l1[ind] <= p:
            ans = ind
        ind += 1

    print(ans)
