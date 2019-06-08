t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    if l[0] == l[1]:
        print(l[0] + l[1])
        
    else:
        while(l[0] > 0 and l[1] > 0 and l[0] != l[1]):
            if l[0] > l[1]:
                l[0] %= l[1]
            else:
                l[1] %= l[0]
        print((l[0] + l[1]) * 2)
