t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    val = 0

    for i in range(n):
        c = 0
        for j in range(i):
            if a[j] % a[i] == 0:
                c += 1
        val = max(val, c)
    print(val)
