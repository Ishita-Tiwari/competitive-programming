t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l1 = []
    start, end = 0, n - 1

    while(end > 0):
##        print("loop1", l[end], l[end - 1])
        if l[end] > l[end - 1]:
            break
        end -= 1

    if end == 0:
        print(end)
        continue
    
    while(end > 0):
##        print("loop2", l[end], l[end - 1])
        if l[end] < l[end - 1]:
            break
        end -= 1
    print(end)
