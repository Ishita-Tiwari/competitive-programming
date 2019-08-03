t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    total = sum(a)
    avg = total / n
    avg1 = 0
    c = -1
    count = 0

    for i in range(n):
        avg1 = (total - a[i]) / (n - 1)
        if avg == avg1:
            if count == 0:
                count += 1
                c = i + 1
            else:
                c = min(c, i + 1)
    if c == -1:
        print("Impossible")
    else:
        print(c)
