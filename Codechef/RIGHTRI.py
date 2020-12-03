n = int(input())
count = 0
for N in range(n):
    
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
    a, b, c = 0, 0, 0

    a = (x1 - x2) ** 2 + (y1 - y2) ** 2
    b = (x2 - x3) ** 2 + (y2 - y3) ** 2
    c = (x3 - x1) ** 2 + (y3 - y1) ** 2

    if a == b + c or b == a + c or c == a + b:
        count += 1
print(count)
