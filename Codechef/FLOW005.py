t = int(input())
for T in range(t):
    n = int(input())
    c = 0
    while(n > 0):
        if n >= 100:
            n -= 100
            c += 1
        elif n >= 50:
            n -= 50
            c += 1
        elif n >= 10:
            n -= 10
            c += 1
        elif n >= 5:
            n -= 5
            c += 1
        elif n >= 2:
            n -= 2
            c += 1
        else:
            n -= 1
            c += 1
    print(c)
