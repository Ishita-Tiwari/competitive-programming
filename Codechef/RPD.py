t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    mx = 0
    sm, ans = 0, 0
    sm1 = 0
    for i in range(n):
        for j in range(i + 1, n):
            sm = 0
            prod = l[i] * l[j]
            while(prod > 0):
                sm += prod % 10
                prod //= 10
            if sm >= sm1:
                sm1 = sm
    print(sm1)
