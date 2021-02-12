t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = set()
    d = {}
    flag = 0
    
    for i in range(n):
        if a[i] not in s:
            d[a[i]] = 1
            s.add(a[i])
        else:
            d[a[i]] += 1
    l = []
    l1 = list(s)
    for i in range(len(s)):
        l.append(d[l1[i]])

    l.sort()
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            flag = -1
            break
##    print(flag)
    s = set()
    
    for i in range(n):
        if a[i] not in s:
            
            val = d[a[i]]
            v1 = 0
            for j in range(i, n):
                if a[i] == a[j]:
                    v1 += 1
                else:
                    break
##            print(a[i], d[a[i]], v1)
            s.add(a[i])
            if v1 != val:
                flag = -1
                break
##    print(flag)
    
    if flag == -1:
        print("NO")
    else:
        print("YES")
    
