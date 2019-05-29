l = [0] * 100
l[0] = 1
for i in range(1, 100):
    l[i] = (i+1) * l[i-1]

t = int(input())
while(t > 0):
    n = int(input()) - 1
    print(l[n])
    t -= 1
