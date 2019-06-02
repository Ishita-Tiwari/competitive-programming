t = int(input())
while(t > 0):
    p = int(input())
    count, i = 0, 11
    while(p > 0):
        if p >= pow(2, i):
            p -= pow(2, i)
            count += 1
            i += 1
        i -= 1
    print(count)
    t -= 1
