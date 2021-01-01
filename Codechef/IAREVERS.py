n = int(input())
ans = []
for N in range(n):
    s = input().strip()
    s1 = ""

    for i in range(len(s)):
        if s[i] != "." and s[i] != "'" and s[i] != "," and s[i] != ";" and s[i] != ":":
            s1 += s[i]

    l = [x for x in s1.split()]
    l.reverse()
    ans.append(l)
for i in range(n - 1, -1, -1):
    print(*ans[i])
