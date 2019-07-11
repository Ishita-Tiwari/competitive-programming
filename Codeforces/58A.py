s = input()
c = 0
s1 = 'hello'
for i in s:
    if i == s1[c]:
        c += 1
    if c == len(s1):
        print("YES")
        break
else:
    print("NO")
