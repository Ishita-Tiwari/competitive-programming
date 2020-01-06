t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    l.sort()
    v1, v2 = 0, 0
    ans = abs(l[0] - l[1]) + abs(l[1] - l[2]) + abs(l[0] - l[2])
    if l[0] == l[1] and l[1] != l[2]:
        if l[2] == l[1] + 1:
            l[2] -= 1
        else:
            l[2] -= 1
            l[1] += 1
            l[0] += 1
        ans = abs(l[0] - l[1]) + abs(l[1] - l[2]) + abs(l[0] - l[2])
        
    elif l[0] != l[1] and l[1] != l[2]:
        l[0] += 1
        l[2] -= 1
        ans = abs(l[0] - l[1]) + abs(l[1] - l[2]) + abs(l[0] - l[2])

    elif l[0] != l[1] and l[1] == l[2]:
        if l[0] == l[1] - 1:
            l[0] += 1
        else:
            l[0] += 1
            l[1] -= 1
            l[2] -= 1
        ans = abs(l[0] - l[1]) + abs(l[1] - l[2]) + abs(l[0] - l[2])
    
    print(ans)
