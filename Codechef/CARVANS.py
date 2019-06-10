t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    c = 1
    for i in range(1, n):
        if l[i] > l[i - 1]:
            l[i] = l[i - 1]
        else:
            c += 1
    print(c)
