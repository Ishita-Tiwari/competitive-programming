t = int(input())
while(t > 0):
    a, b = [int(x) for x in input().split()]
    print(max(a, b), a + b)
    t -= 1
