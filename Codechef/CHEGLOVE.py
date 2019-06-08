t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]
    c, c1 = 0, 0
    for i in range(n):
        if l[i] > g[i]:
            c = -1
        if l[i] > g[n - 1 - i]:
            c1 = -1
    if c == 0 and c1 == 0:
        print("both")
    elif c == 0:
        print("front")
    elif c1 == 0:
        print("back")
    else:
        print("none")
