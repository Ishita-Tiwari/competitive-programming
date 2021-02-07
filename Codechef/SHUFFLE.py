t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if k == 1 or sorted(a) == a:
        print("yes")
        continue
    l = [[] for i in range(k)]

    for i in range(n):
        l[i % k].append(a[i])
##    print(l)

    for i in range(k):
        l[i].sort()

##    print(l)
    final = [0] * n

    for i in range(k):
        for j in range(len(l[i])):
            final[i + j * k] = l[i][j]
        

    if final == sorted(a):
        print("yes")
    else:
        print("no")
