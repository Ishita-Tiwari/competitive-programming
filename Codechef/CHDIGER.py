t = int(input())
for T in range(t):
    n, d = [x for x in input().split()]
    l = list(n)
    a = [l[0]]
    c = 0
    
    for i in range(1, len(l)):
        if (l[i] >= a[-1]):
            a.append(l[i])
        else:
            while(len(a) > 0 and a[-1] > l[i]):
                a = a[:len(a)-1]
            a.append(l[i])
            
    for i in a:
        if i <= d:
            print(i, end='')
            c += 1
        else:
            break
    print(d*(len(l)-c))
