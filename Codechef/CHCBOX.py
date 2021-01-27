t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    mx = max(l)
    cmx = l.count(mx)
    l1 = [0] * n
    for i in range(n): #l1 marks mx
        if l[i] == mx:
            l1[i] = 1

    v1, v2 = sum(l1[:n // 2 + 1]), sum(l1[n // 2 + 1:])
    
    count = 0
##    if v1 == 0:
##        print("0")
##        continue
##    count = 0
    ind = n // 2 - 1
    for i in range(0, n):
        v1 -= l1[ind]
        v1 += l1[n - i - 1]
        
        v2 += l1[ind]
        v2 -= l1[n - i - 1]
        
        
        if v1 == 0:
            count += 1
##        print(n - i - 1, ind, v1, count)
        if ind == 0:
            ind = n - 1
        else:
            ind -= 1
        
##        if ind == -1:
##            ind = n - 1
        
            
    print(count)
