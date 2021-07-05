t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    s = input()
    l = list(s)
    l = [int(x) for x in l]
    mn = min(l.count(0), m)
##    print(l, mn)

    while(mn):
        ind = 0
        curr = set()
        for i in range(n):
            if i > 0 and i < n - 1 and (i not in curr): 
##                print("in1", i)
                if l[i] == 1:
                    if (i - 2 > -1 and l[i - 2] != 1 and l[i - 1] != 1) or (i == 1 and l[i - 1] != 1) or (i - 2 > -1 and l[i - 2] == 1 and l[i - 1] != 1 and i - 2 in curr):
                        l[i - 1] = 1
                        curr.add(i - 1)
                    if (i + 2 < n and l[i + 2] != 1 and l[i + 1] != 1) or (i == n - 2 and l[i + 1] != 1) or (i + 2 < n and l[i + 2] == 1 and l[i + 1] != 1 and i + 2 in curr):
                        l[i + 1] = 1
                        curr.add(i + 1)
            elif i == 0 and (i not in curr):
                if l[i] == 1:
                    if i + 1 == n - 1 and l[i + 1] != 1:
                        l[i + 1] = 1
                        curr.add(i + 1)
                    if (i + 2 < n and l[i + 2] != 1 and l[i + 1] != 1) or (i + 2 < n and l[i + 2] == 1 and l[i + 1] != 1 and i + 1 in curr):
                        l[i + 1] = 1
                        curr.add(i + 1)
            elif i == n - 1 and (i not in curr):
##                print("YESSSS")
                if l[i] == 1 and i - 1 > -1 and l[i - 1] != 1:
                    if i - 1 == 0:
                        l[i - 1] = 1
                        curr.add(i - 1)
                    if (i - 2 > -1 and l[i - 2] != 1) or (i - 2 > -1 and l[i - 2] == 1 and i - 2 in curr):
                        l[i - 1] = 1
                        curr.add(i - 1)
##        print(curr, l)
##                    
##        print(*l)
        mn -= 1
    l = [str(x) for x in l]
    ans = ''.join(l)
    print(ans)
