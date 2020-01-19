t = int(input())
for T in range(t):
    n, p, k = [int(x) for x in input().split()]
    p1 = p
    l = [int(x) for x in input().split()]
    v1, v2 = 0, 0
    l.sort()
    
    for i in range(1, n, 2):
        if l[i] <= p:
            p -= l[i]
            v1 += 2
        else:
            if l[i - 1] <= p:
                p -= l[i - 1]
                v1 += 1
 
    if n % 2 == 1:
        if l[-1] <= p:
            v1 += 1
            p -= l[-1]
    p = p1
    for i in range(0, n, 2):
        if l[i] <= p:
            p -= l[i]
            if i == 0: v2 += 1
            else: v2 += 2
        else:
            if i > 0 and l[i - 1] <= p:
                p -= l[i - 1]
                v2 += 1
 
    if n % 2 == 0:
        if l[-1] <= p:
            v2 += 1
 
    print(max(v1, v2))
