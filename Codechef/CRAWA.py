t = int(input())
for T in range(t):
    x, y = [int(x) for x in input().split()]
    if x > 0 and x % 2 == 1 and y > -x + 1 and y <= x + 1:
        print("YES")
    elif x < 0 and x % 2 == 0 and y >= x and y <= -x:
        print("YES")
    elif y > 0 and y % 2 == 0 and x >= -y and x < y:
        print("YES")
    elif y <=0 and y % 2 == 0 and x >= y and x <= -y + 1:
        print("YES")
    else:
        print("NO")
