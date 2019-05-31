t = int(input())
while(t > 0):
    n = input()
    l = list(n)
    sumFL = int(l[0]) + int(l[len(n)-1])
    print(sumFL)
    t -= 1
