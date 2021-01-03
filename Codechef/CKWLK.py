for i in range(int(input())):
    n = int(input())
    val = 0
    count = 0
    while(True):
        if n % 10 == 0:
            n //= 10
            count += 1
        else:
            break
    c = -1
    for i in range(0, 3000):
        if n == pow(2, i):
            c = i
            break
        if n < pow(2, i):
            break
    if count < c:
        c = -1
    if c == -1:
        print("No")
    else:
        print("Yes")
