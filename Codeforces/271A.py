y = int(input())
y1 = y
c = -1
while(c == -1):
    y1 += 1
    c = 0
    l = list(str(y1))
    l.sort()
    for i in range(3):
        if l[i] == l[i+1]:
            c = -1
print(y1)
