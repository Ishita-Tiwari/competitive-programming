t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    k = int(input())
    x = int(input())
    s1, s2 = 0, 0
    l = []
    if k == n:
        for i in range(n):
            s1 += a[i]
            s2 += a[i] ^ x
        print(max(s1, s2))
    else:
        if k % 2 != 0:
            for i in range(n):
                s1 += max(a[i], a[i] ^ x)
            print(s1)
        else:
            for i in range(n):
                l.append((a[i] ^ x) - a[i])
            l.sort(reverse = True)
            s1 = sum(a)
            h, diff = 0, 0
            for i in range(n):
                diff += l[i]
                if(i % 2 == 1 and diff > h):
                    h = diff
            print(s1 + h)
