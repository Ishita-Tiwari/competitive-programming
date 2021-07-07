t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    c = 0
    beg, end = -1, -1
    
    for i in range(n):
        if l[i] % k == 0:
            c += 1
        else:
            end = i
            if beg == -1:
                beg = i

    if c == n:
        print(-1)
        continue
    if sum(l) % k:
        print(n)
        continue
    print(max(n - beg - 1, end))
