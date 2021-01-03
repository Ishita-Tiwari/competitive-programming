t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    while(len(a) > 2):
        least = min(a[:3])
        most = max(a[:3])
        mid = sum(a[:3]) - least - most
##        print(a, least, mid, most)
        
        del a[a.index(mid)]
    if n % 2 == 2:
        a.reverse()
    print(*a)
