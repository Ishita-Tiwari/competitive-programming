t = int(input())
for T in range(t):
    n, x = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    total = 0
    c = 0
    for i in range(n):
        total += l[i]
    num = total // x
    for i in range(n):
        if (total - l[i]) // x == num:
            c = 1
            break
    if c == 1:
        print("-1")
    else:
        print(num)
