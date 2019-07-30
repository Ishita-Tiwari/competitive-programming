for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if sum(a) % 4 != 0:
        print(-1)
    else:
        count = 0
        a1 = 0
        a2 = 0
        a3 = 0
        for i in a:
            if i%4 == 1:
                a1 += 1
            elif i%4 == 2:
                a2 += 1
            elif i%4 == 3:
                a3 += 1
        m = min(a1,a3)
        count += m
        a1 -= m
        a3 -= m
        a2 += a1//2 + a3//2
        count += a1//2+a3//2+a2//2
        print(count)
        
