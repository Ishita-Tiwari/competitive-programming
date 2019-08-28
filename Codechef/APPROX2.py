t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    val = abs(a[0] + a[1] - k)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if val == abs(a[i] + a[j] - k):
                ##print(i+1, j+1, a[i], a[j], k, abs(a[i] + a[j] - k))
                c += 1
            elif val > abs(a[i] + a[j] - k):
                val = abs(a[i] + a[j] - k)
                c = 1
            else:
                continue
    print(val, c)
