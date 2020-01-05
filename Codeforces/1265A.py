def check(s):
    n = len(s)
    flag = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            flag = -1
            break
    if flag == -1:
        print(-1)
    else:
        ans = ""
        for i in range(n):
            ans += s[i]
        print(ans)

t = int(input())
for T in range(t):
    s = input()
    n = len(s)
    ans = s
    s = list(s)
    if n == 1:
        if s[0] == '?':
            s[0] = 'a'
        print(*s)
    elif s.count('?') == n:
        ans = "abc" * (n // 3)
        for i in range(n - len(ans)):
            if i % 3 == 0:
                ans += 'a'
            elif i % 3 == 1:
                ans += 'b'
            else:
                ans += 'c'
        print(ans)
    else:
        for i in range(n):
            if s[i] != '?':
                continue
            if i == 0:
                if s[i + 1] == '?':
                    s[i] = 'a'
                elif s[i + 1] == 'a':
                    s[i] = 'b'
                elif s[i + 1] == 'b':
                    s[i] = 'c'
                else:
                    s[i] = 'a'
            elif i == n - 1:
                if s[i - 1] == 'a':
                    s[i] = 'b'
                elif s[i - 1] == 'b':
                    s[i] = 'c'
                else:
                    s[i] = 'a'
            else:
                if s[i - 1] == 'a':
                    if s[i + 1] == 'b': s[i] = 'c'
                    else: s[i] = 'b'
                elif s[i - 1] == 'b':
                    if s[i + 1] == 'a': s[i] = 'c'
                    else: s[i] = 'a'
                else:
                    if s[i + 1] == 'b': s[i] = 'a'
                    else: s[i] = 'b'
        check(s)
