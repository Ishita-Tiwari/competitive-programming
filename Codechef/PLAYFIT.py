t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    suff, pref = l[:], l[:]

    for i in range(1, n):
        pref[i] = min(pref[i], pref[i - 1])
    for i in range(n - 2, -1, -1):
        suff[i] = max(suff[i], suff[i + 1])
    ans = 0
    for i, j in zip(suff, pref):
        ans = max(ans, i - j)

    if ans <= 0:
        print("UNFIT")
    else:
        print(ans)
