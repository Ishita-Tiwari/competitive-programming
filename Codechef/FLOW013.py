t = int(input())
for T in range(t):
    a, b, c = [int(x) for x in input().split()]
    total = a + b + c
    if total == 180:
        print("YES")
    else:
        print("NO")
