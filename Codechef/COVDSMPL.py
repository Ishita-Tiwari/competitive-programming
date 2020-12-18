t = int(input())
for T in range(t):
    n, p = [int(x) for x in input().split()]
    l = [[0 for x in range(n)] for x in range(n)]
    r, c = 0, 0
    count = 0
    while(count < n * n and c < n):
        
        if r == n:
            c += 1
            r = 0

        pr = r + 1
        pc = c + 1
        if pr > n or pc > n:
            break
        print(1, pr, pc, pr, pc)
        inp = int(input())

        l[r][c] = inp
        count += 1
        r += 1

    print(2)
    for i in range(n):
        print(*l[i])

    x = int(input())
    if x == -1:
        break
