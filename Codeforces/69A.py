n = int(input())
X, Y, Z = [0] * 3
for N in range(n):
    x, y, z = [int(x) for x in input().split()]
    X += x
    Y += y
    Z += z
if X == 0 and Y == 0 and Z == 0:
    print("YES")
else:
    print("NO")
