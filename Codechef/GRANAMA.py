t = int(input())
for T in range(t):
    l = [x for x in input().split()]
    l1 = list(l[0])
    l2 = list(l[1])
    l1.sort()
    l2.sort()
    s1, s2 = "", ""
    for i in range(len(l1)):
        if l1[i] not in s1:
            s1 += l1[i]
    for i in range(len(l2)):
        if l2[i] not in s2:
            s2 += l2[i]
    if s1 != s2:
        print("YES")
    else:
        if l1 == l2:
            print("YES")
        else:
            print("NO")
