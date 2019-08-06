from math import ceil
t = int(input())
for T in range(t):
    xf = int(input())
    x, y = 0, 0
    p = 1
    val = 0
    while(x <= xf):
        ##print(x, y, p)
        x = p
        y += (p * p)
        p = ceil(y ** 0.5)
        val += 1
    print(val - 2)
