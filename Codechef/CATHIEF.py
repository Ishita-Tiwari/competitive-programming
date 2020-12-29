t = int(input())
for T in range(t):
    x, y, k, n = [int(i) for i in input().split()]
    if abs(x - y) % (k * 2) == 0:
        print("Yes")
    else:
        print("No")
