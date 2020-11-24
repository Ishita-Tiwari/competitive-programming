t = int(input())
for T in range(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 != x2 and y1 != y2:
        print("sad")
        continue
    if x1 < x2:
        print("right")
    elif x1 > x2:
        print("left")
    elif y1 < y2:
        print("up")
    else:
        print("down")
