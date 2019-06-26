t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    x, ans = 0, 0
    l = [0] * 32
    for i in range(n):
        lis = list(bin(a[i])[2:])[::-1]
        for j in range(len(lis)):
            l[j] += int(lis[j])

    for i in range(32):
        if l[i] > (n // 2):
            x += (1 << i)
    for i in a:
        ans += (i ^ x)
    print(ans)            

