t = int(input())
for T in range(t):
    l = ['0'] * 3
    n = int(input())
    if 360 % n == 0:
        l[0] = 'y'
    else:
        l[0] = 'n'
    if n <= 360:
        l[1] = 'y'
    else:
        l[1] = 'n'
    if 360 >= (n * (n + 1)) / 2:
        l[2] = 'y'
    else:
        l[2] = 'n'
    print(*l)
