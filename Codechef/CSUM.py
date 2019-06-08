t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort()
    lb, ub, total, c = 0, n-1, 0, 0
    while(ub > lb):
        total = l[lb] + l[ub]
        if total > k:
            ub -= 1
        elif total < k:
            lb += 1
        else:
            c = 1
            break
    if c == 1:
        print("Yes")
    else:
        print("No")
