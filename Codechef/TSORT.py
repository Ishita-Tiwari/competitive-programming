t = int(input())
l = [0] * t
for i in range(t):
    l[i] = int(input())
l.sort()
for i in range(t):
    print(l[i])
