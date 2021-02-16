t = int(input())
for T in range(t):
    n = int(input())
    w = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]

    if n == 2:
        ans = 0
        ind2, ind1 = w.index(2), w.index(1)
        two, one = ind2 + 1, ind1 + 1
        
        while(two <= one):
            two += l[ind2]
            ans += 1
        print(ans)
        
    elif n == 3:
        ans = 0
        ind3, ind2, ind1 = w.index(3), w.index(2), w.index(1)
        three, two, one = ind3 + 1, ind2 + 1, ind1 + 1
        
        while(two <= one):
            two += l[ind2]
            ans += 1
        while(three <= two):
            three += l[ind3]
            ans += 1
        print(ans)

    else:
        ans = 0
        ind4, ind3, ind2, ind1 = w.index(4), w.index(3), w.index(2), w.index(1)
        four, three, two, one = ind4 + 1, ind3 + 1, ind2 + 1, ind1 + 1
        
        while(two <= one):
            two += l[ind2]
            ans += 1
        while(three <= two):
            three += l[ind3]
            ans += 1
        while(four <= three):
            four += l[ind4]
            ans += 1
        print(ans)
