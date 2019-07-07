s = input()
l = list(s)
c0, c1 = 0, 0
for i in range(len(s)):
    if l[i] == '1' and c0 < 7:
        c1 += 1
        c0 = 0
    if l[i] == '0' and c1 < 7:
        c0 += 1
        c1 = 0
if c0 >= 7 or c1 >= 7:
    print("YES")
else:
    print("NO")
