s = input()
s1 = ''
for letter in "+":
    s = s.replace(letter, '')
l = list(s)
l.sort()
for i in range(len(s)):
    if i < len(s)-1:
        s1 += l[i] + "+"
    else:
        s1 += l[i]
print(s1)
