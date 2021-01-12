t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = ""
    val = l[0]
    if n == 1:
        print(*l)
        continue
    val1 = l[1]
    s += str(l[0])
    count = 0
    for i in range(1, n):
        v1 = l[i]
        
        if l[i] == l[i - 1] + 1:
##            print(l[i])
            val = l[i]
            count += 1
            if i == n - 1:
                if count == 1:
                    s += "," + str(l[i])
                else:
                    s += "..." + str(l[i])
        else:
##            print(l[i])
            if count == 0:
                s += "," + str(v1)
            elif count == 1:
                s += "," + str(val) + "," + str(l[i])
            else:
                s += "..." + str(val) + "," + str(l[i])
            count = 0

    print(s)
