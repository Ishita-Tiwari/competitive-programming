def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return(f)

t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    l, d = a[:k], {}
    for i in range(k, n):
        if a[i] == l[k - 1]:
            l.append(a[i])
        else:
            break
    s = set(l)
    l1 = list(s)
    l1.sort()
    for i in l1:
        d[i] = 0
    for i in l:
        d[i] += 1


    if len(s) == 1:
        #print("case 1")
        if k == 1:
            ans = d[l[0]]
        else:
            ans = fact(d[l[0]]) // (fact(k) * fact(d[l[0]] - k))
    elif len(s) == 2:
    #print("case 2")
        v1 = 0
        if d[l1[0]] > 1:
            v1 = fact(d[l1[0]]) // (fact(k) * fact(d[l1[0]] - k))
        v2 = fact(d[l1[1]]) // (fact(k - d[l1[0]]) * fact(d[l1[1]] - k + d[l1[0]]))
        ans = v2 - v1
    else:
        #print("case 3")
        v1 = 0
        for i in range(len(l1) - 1):
            #print(i, l1[i], d[l1[i]])
            v1 += d[l1[i]]
        ans = fact(d[l[-1]]) // (fact(k - v1) * fact(d[l[-1]] - k + v1))
    print(ans)

