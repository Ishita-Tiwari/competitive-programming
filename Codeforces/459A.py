x1, y1, x2, y2 = [int(x) for x in input().split()]
if x1 == x2 or y1 == y2:
    dist = abs(x1 - x2) + abs(y1 - y2)
    if x1 == x2:
        '''others are on left or right'''
        x3 = x1 + dist
        x4 = x1 - dist
        if x3 <= 1000:
            print(x3, y1, x3, y2)
        elif x4 >= -1000:
            print(x4, y1, x4, y2)
        else:
            print(-1)

    else:
        '''others are above or below'''
        y3 = y1 + dist
        y4 = y1 - dist
        if y3 <= 1000:
            print(x1, y3, x2, y3)
        elif y4 >= -1000:
            print(x1, y4, x2, y4)
        else:
            print(-1)
else:
    if abs(x1 - x2) != abs(y1 - y2):
        print(-1)
    else:
        print(x1, y2, x2, y1)
