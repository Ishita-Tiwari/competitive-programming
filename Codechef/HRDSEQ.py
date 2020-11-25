l = [0, 0]
s = set(l)
l.append(1)
for i in range(129):
    val = l[-1]
##    print(l, val, s)
    ind = 0
    if val not in s:
        l.append(0)
    else:
        for j in range(len(l) - 2, -1, -1):
            if l[j] == val:
                ind = j
                break
        l.append(len(l) - ind - 1)
        s = set(l[:len(l) - 1])

t = int(input())
for T in range(t):
    n = int(input())
    val = l[n - 1]
    l1 = l[:n]
    print(l1.count(val))
