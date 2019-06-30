t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ans = 0

    odd, even = [], []
    vis = [0] * n
    bans = [-1] * n
    done = 0
    for i in b:
        if i & 1:
            odd.append(i)
        else:
            even.append(i)

    cur = 0
    cnt = len(odd)
    for i in range(n):
        if a[i] & 1:
            bans[i] = odd[cur]
            cur += 1
            if cur == cnt:
                done = 1
                break


    if not done:
        for i in range(n):
            if bans[i] == -1:
                bans[i] = odd[cur]
                cur += 1
                if cur == cnt:
                    break
    #print(bans, done)
    cur = 0
    ans = 0
    for i in range(n):
        if bans[i] == -1:
            bans[i] = even[cur]
            cur += 1

    for i, j in zip(a, bans):
        ans += (i + j) // 2
    print(ans)
