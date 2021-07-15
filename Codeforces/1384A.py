t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    mx = max(a)
    if mx == 0:
        mx = 1
    ans = ['a' * mx]
    nxt = 'a' * a[0] + 'b' * (mx - a[0])
    ans.append(nxt)
    for i in range(1, n):
        val = a[i]
        prev = ans[-1]
        nxt = prev[:a[i]]
        if a[i] < len(prev):
            if prev[a[i]] == 'b':
                nxt += 'a'
            if prev[a[i]] == 'a':
                nxt += 'b'
            rest = prev[a[i] + 1:]
            nxt += rest
        
        ans.append(nxt)

    for i in ans:
        print(i)
