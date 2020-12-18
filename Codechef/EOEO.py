p = []
val = 1
for i in range(61):
    p.append(val)
    val *= 2

t = int(input())
for T in range(t):
    ts = int(input())
    ans = 0

    if ts % 2:
        ans = ts // 2
    else:
        mx = 0
        for i in range(59, -1, -1):
            if ts % p[i] == 0:
                ts //= p[i]
                break
        ans = ts // 2

    print(ans)
