def powerSet(l, n, m):
    powsize = int(2 ** n)
##    print(powsize)
    counter = 0
    j = 0
    val = 0
    flag = 0
    for counter in range(powsize):
        l1 = []
        for j in range(n):
            if (counter & (1 << j)) > 0:
                l1.append(l[j])
##        print(l1)
        if sum(l1) == m:
            flag = 1
    
    return(flag)


t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    l = []
    for i in range(n):
        l.append(int(input()))

    if powerSet(l, n, m):
        print("Yes")
    else:
        print("No")
