t = int(input())
for T in range(t):
    n, b = [int(x) for x in input().split()]
    W, H, P, j = 0, 0, 0, 0
    p, a = [0] * n, [0] * n
    c = 0
    for i in range(n):
        W, H, P = [int(x) for x in input().split()]
        if P <= b:
            c = 1
            a[i] = W * H
            p[j] = P
    if c == 0:
        print("no tablet")
    else:
        print(max(a))
