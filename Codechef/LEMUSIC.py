t = int(input())
for T in range(t):
    n = int(input())
    val = []
    s = set()
    for i in range(n):
        val.append([int(x) for x in input().split()][::-1])
    val.sort()

    c = 0
    c1 = 0
    ans = 0
    for i in range(n):
        if val[i][1] not in s:
            s.add(val[i][1])
            c += 1
            ans += (c * val[i][0])
        else:
            c1 += val[i][0]

    ans += (c * c1)

    print(ans)
