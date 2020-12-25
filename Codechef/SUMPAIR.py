t = int(input())
for T in range(t):
    n, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse = True)
    
    ind, ind1 = 0, 1
    ans = []
    while(ind < n - 1):
        if a[ind] - a[ind + 1] < d:
            ans.append(a[ind])
            ans.append(a[ind + 1])
            ind += 2
            continue
        ind += 1

    print(sum(ans))
