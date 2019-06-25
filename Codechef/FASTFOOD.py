t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a1 = [0] * n
    b1 = [0] * n

    a1[0] = a[0]
    b1[n - 1] = b[n - 1]
    for i in range(1, n):
        a1[i] = a[i] + a1[i - 1]
    
    for i in range(n - 2, -1, -1):
        b1[i] = b1[i + 1] + b[i]
    mx = b1[0]
    for i in range(n - 1):
        mx = max(mx, a1[i] + b1[i + 1])
    mx = max(mx, a1[n - 1])
    
    print(mx)
