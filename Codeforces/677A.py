n, h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
w = 0
for i in a:
    if i > h:
        w += 2
    else:
        w += 1
print(w)
