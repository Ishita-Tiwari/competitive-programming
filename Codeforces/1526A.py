t = int(input())
for T in range(t):
    n = int(input())
    n *= 2
    a = [int(x) for x in input().split()]
    a.sort()

    b = [0] * n
    ind = 0
    for i in range(0, n, 2):
        b[i] = a[ind]
        ind += 1
    for i in range(1, n, 2):
        b[i] = a[ind]
        ind += 1

    print(*b)
