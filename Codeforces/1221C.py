t = int(input())
for T in range(t):
    c, m, x = [int(x) for x in input().split()]
    mn, mx = min(c, m), max(c, m)

    diff = mx - mn
    x += diff
    if c > m: c -= diff
    else: m -= diff

    tp1 = min(c, m, x)
    c, m, x = c - tp1, m - tp1, x - tp1

    tp1 += (c + m) // 3
    print(tp1)
