l = list(input())
low, up = 0, 0
s = ''
for i in range(len(l)):
    if l[i].isupper() == True:
        up += 1
    else:
        low += 1
for i in range(len(l)):
    if up > low:
        s += l[i].upper()
    else:
        s += l[i].lower()
print(s)
