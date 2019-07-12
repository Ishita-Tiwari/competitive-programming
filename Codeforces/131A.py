l = list(input())
c = 0
for i in range(1, len(l)):
    if l[i].islower() == True:
        c = -1
        break
s = ""
for i in range(len(l)):
    if c == 0:
        if i == 0:
            if l[i].islower() == True:
                s += l[i].upper()
            if l[i].isupper() == True:
                s += l[i].lower()
        else:
            s += l[i].lower()
    else:
        s += l[i]
print(s)
