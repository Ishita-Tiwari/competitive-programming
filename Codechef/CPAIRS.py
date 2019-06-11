t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    ans, c = 0, 0
    for i in range(n):
        if l[i] % 2 == 0:
            c += 1
        else:
            ans += c
    print(ans)
