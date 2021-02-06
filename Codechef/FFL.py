t = int(input())
for T in range(t):
    n, s = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    df = [int(x) for x in input().split()]

    d = []
    f = []

    for i in range(n):
        if df[i] == 0:
            d.append(p[i])
        else:
            f.append(p[i])
    if len(d) < 1 or len(f) < 1:
        print("no")
        continue
    
    d.sort()
    f.sort()

    if s + d[0] + f[0] <= 100:
        print("yes")
    else:
        print("no")
