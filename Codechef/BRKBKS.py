t = int(input())
for T in range(t):
    s, w1, w2, w3 = [int(x) for x in input().split()]
    ans = 0
    if w1 + w2 + w3 <= s:
        ans = 1
    else:
        if w1 + w2 <= s:
            ans = 2
        elif w3 + w2 <= s:
            ans = 2
        else:
            ans = 3
    print(ans)
