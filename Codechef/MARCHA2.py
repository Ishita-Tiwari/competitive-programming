t = int(input())
for T in range(t):
    k = int(input())
    flag = True
    stems = 1.0
    l = [int(x) for x in input().split()]
    
    for i in range(k):
        if l[i] > stems:
            flag = False
            break
        else:
            stems = 2 * (stems - l[i])
    
    if flag == True and stems == 0:
        print("Yes")
    else:
        print("No")
