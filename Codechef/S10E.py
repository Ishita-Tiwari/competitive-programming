t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 1
    val = 0

    for i in range(1, n):
        c = 0
        for j in range(max(0, i - 5), i):
            if a[i] >= a[j]:
                c = -1
        if c == 0:
            ans += 1
            val = a[i]
    print(ans)
