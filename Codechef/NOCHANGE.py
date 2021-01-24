t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]

    a = l[:]
    a.sort(reverse = True)
    d = {}
    k1 = k
    for i in range(n):
        d[a[i]] = 0
    ind, val, done, sm = [0] * 4
    latest, latval = 0, 0
    
    while(sm < k and ind < n):
        if (k - sm) % a[ind] == 0:
            val = (k - sm) // a[ind] - 1
            d[a[ind]] = val
            done = val * a[ind]
            sm += done
            latest = a[ind]
            latval = val
        else:
            val = (k - sm) // a[ind] + 1
            d[a[ind]] = val
            done = val * a[ind]
            sm += done
            latest = a[ind]
            latval = val
##        print(a[ind], done)
        ind += 1

    if (sm > k1 and sm - latest < k1) == False:
        print("NO")
        continue
    ans = []
    for i in range(n):
        ans.append(d[l[i]])
    print("YES", *ans)
