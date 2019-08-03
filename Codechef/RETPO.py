t = int(input())
for T in range(t):
    x, y = [int(x) for x in input().split()]
    x = abs(x)
    y = abs(y)
    ans = 0
    if x == y or y == x + 1:
        ans = x + y
    else:
        if x > y:
            ans = (2 * y) + (2 * (x - y)) + (x - y) %  2
        else:
            ans = (2 * x) + (2 * (y - x - 1)) + (y - x - 1) % 2 + 1
    print(ans)
