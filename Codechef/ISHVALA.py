t = int(input())
for T in range(t):
    n, m = [int(_) for _ in input().split()]
    x, y, s = [int(_) for _ in input().split()]
    lx, ly = [], []
    if x > 0:
        lx = [int(_) for _ in input().split()]
    if y > 0:
        ly = [int(_) for _ in input().split()]
        
    dx, dy = [], []

    if m not in ly:
        ly.append(m + 1)
    if n not in lx:
        lx.append(n + 1)

    val = lx[0] - 1
    dx.append(val)
    val = ly[0] - 1
    dy.append(val)

    for i in range(1, len(lx)):
        val = lx[i] - lx[i - 1] - 1
        dx.append(val)
##        print(lx, lx[i], val)
    for i in range(1, len(ly)):
        val = ly[i] - ly[i - 1] - 1
        dy.append(val)
##    print(dx)
##    print(dy)

    total_x = []
    total_y = []
    for i in dx:
        total_x.append(i // s)
    for i in dy:
        total_y.append(i // s)

    sum_x = sum(total_x)
    sum_y = sum(total_y)

    print(sum_x * sum_y)
