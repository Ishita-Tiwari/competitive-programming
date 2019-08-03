t = int(input())
for T in range(t):
    s = list(input())
    c = 0
    val = ""
    if s == s[::-1]:
        print("YES")
        continue
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            ind = i
            val = s[:ind] + s[ind + 1:]
            if val == val[::-1]:
                c = 1
            ind = len(s) - i - 1
            val = s[:ind] + s[ind + 1:]
            if val == val[::-1]:
                c = 1
            break
    if c == 0:
        print("NO")
    else:
        print("YES")
