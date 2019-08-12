t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = 0
    val = []

    for i in range(n):
        c = a[i] * 20 - b[i] * 10
        if c < 0:
            c = 0
        val.append(c)
    print(max(val))
