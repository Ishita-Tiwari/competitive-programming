t = int(input())
for T in range(t):
    m, w = [x for x in input().split()]
    l1 = list(m)
    l2 = list(w)
    c, c1 = 0, 0
    if len(m) < len(w):
        l1, l2 = list(w), list(m)
    while(c < len(l1) and c1 < len(l2)):
        if l1[c] == l2[c1]:
            c1 += 1
        c += 1
    if c1 == len(l2):
        print("YES")
    else:
        print("NO")
