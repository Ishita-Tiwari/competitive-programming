n = int(input())
ans = ''
for N in range(n):
    s = input()
    s.lower
    for i in range(len(s)):
        if s[i] != "." and s[i] != "'" and s[i] != "," and s[i] != ";" and s[i] != ":":
            ans += s[i]

ans = ans.lower()
ans = ans.split()
ans = list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
