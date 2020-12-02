t = int(input())
for T in range(t):
    s = input()
    n = len(s)
    val, s1 = 0, ""
    ch = s[0]
    ans = "NO"
    for i in range(n):
        if s[i] == ch:
            val += 1
        else:
            s1 += (ch + str(val))
            val = 1
            ch = s[i]
    s1 += (ch + str(val))
    if len(s1) < n:
        ans = "YES"
    print(ans)
