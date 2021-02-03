t = int(input())
for T in range(t):
    n = int(input())
    l = []
    ind = 0
    for i in range(1, n, 2):
##        print(i, l)
        l.append([i, i + 1])
##        ind += 1
    if n == 1:
        print(1)
        print(1, 1)
        continue
    if n % 2 == 1:
        l[0].append(n)
    print(len(l))
    for i in range(len(l)):
        print(len(l[i]), *l[i])
