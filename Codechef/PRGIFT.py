t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    c = 0
    for i in a:
        if i % 2 == 0:
            c += 1
    if k == 0:
        if c < n:
            print("YES")
        else:
            print("NO")
    else:
        if c >= k:
            print("YES")
        else:
            print("NO")
