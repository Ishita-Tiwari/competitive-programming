t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    for i in range(n):
        a[i] = a[i] % 3

    c0, c1, c2 = a.count(0), a.count(1), a.count(2)

    if c0 == c1 and c1 == c2:
        print(0)
        continue
    ans = 0

    ans = max(c1-c0, c2-c1, c0-c2)
    
    print(ans)
