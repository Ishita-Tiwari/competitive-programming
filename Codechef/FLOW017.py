t = int(input())
while(t > 0):
    a, b, c = [int(x) for x in input().split()]
    l = [a, b, c]
    l.sort()
    print(l[1])
    t -= 1
