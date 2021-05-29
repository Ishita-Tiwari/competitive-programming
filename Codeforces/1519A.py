from math import ceil

t = int(input())
for T in range(t):
    r, b, d = [int(x) for x in input().split()]
    mn, mx = min(r, b), max(r, b)

    diff = mx - mn
##    print(diff)
    if d == 0:
        if r == b:
            print("YES")
        else:
            print("NO")
        continue
    
    num_packets = ceil(diff / d)
##    print(num_packets, "\n")
    
    if mn >= num_packets:
        print("YES")
    else:
        print("NO")
