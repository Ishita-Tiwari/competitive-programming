t = int(input())
for T in range(t):
    input()
    xa, ya = [int(x) for x in input().split()]
    xb, yb = [int(x) for x in input().split()]
    xf, yf = [int(x) for x in input().split()]
    ans = abs(xa - xb) + abs(ya - yb)
    if xa == xb and xa == xf and ((ya < yf and yf < yb) or (ya > yf and yf > yb)):
        ans += 2
    elif ya == yb and ya == yf and ((xa < xf and xf < xb) or (xa > xf and xf > xb)):
        ans += 2

    print(ans)
