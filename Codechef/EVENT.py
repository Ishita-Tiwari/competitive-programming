days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

t = int(input())
for T in range(t):
    s, e, l, r = [x for x in input().split()]
    l, r = int(l), int(r)
    c, ans = 0, 0
    st = [0] * (r - l + 1)
    for i in range(r - l + 1):
        st[i] = l + i
    if days.index(e) >= days.index(s):
        dur = days.index(e) - days.index(s) + 1
    else:
        dur = 8 - days.index(s) + days.index(e)
    dur %= 7
    st = set(st)
    for i in range(l, r + 1):
        if i % 7 == dur:
            c += 1
            if c == 1:
                ans = i
            if c > 1:
                break
    if c == 1:
        print(ans)
    elif c > 1:
        print("many")
    else:
        print("impossible")
