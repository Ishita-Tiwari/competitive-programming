while(True):
    a, b, c = [int(x) for x in input().split()]
    if a == b and b == c and c == 0:
        break
    if(b - a == c - b):
        nxt = c + (c - b)
        print("AP", nxt)
    else:
        nxt = c * (c // b)
        print("GP", nxt)
