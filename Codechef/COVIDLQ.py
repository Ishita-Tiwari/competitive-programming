t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    ind = []
    for i in range(n):
        if l[i]:
            ind.append(i)

    d = [0] * (len(ind) - 1)
    for i in range(1, len(ind)):
        d[i - 1] = ind[i] - ind[i - 1]
        
##    print(ind, d)
    if len(d) < 1:
        print("YES")
        continue
    if min(d) < 6:
        print("NO")
    else:
        print("YES")
