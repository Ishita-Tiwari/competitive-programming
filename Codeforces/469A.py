n = int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
c = 0
l = [0] * (x[0] + y[0]) 
for i in range(1, x[0] + 1):
    l[c] = x[i]
    c += 1
for i in range(1, y[0] + 1):
    l[c] = y[i]
    c += 1
s = len(set(l))
if s >= n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
