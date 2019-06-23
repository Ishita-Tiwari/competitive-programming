from math import ceil
for T in range(int(input())):
    n = [int(x) for x in input()]
    avail = sum(n)

    req = ceil(avail / 10) * 10 - avail
    for i in n:
        print(i, end = '')
    print(req)
