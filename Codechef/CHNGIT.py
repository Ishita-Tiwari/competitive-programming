t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}

    for i in range(n):
        d[a[i]] = 0
    for i in range(n):
        d[a[i]] += 1
    val = 0
    
    for i in range(n):
        val = max(val, d[a[i]])
    print(n - val)
