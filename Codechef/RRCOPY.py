t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    c = n
    for i in range(n - 1):
        if l[i] == l[i + 1]:
            c -= 1
    print(c)
