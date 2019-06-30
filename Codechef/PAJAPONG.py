t = int(input())
for T in range(t):
    x, y, k = [int(x) for x in input().split()]
    pts = x + y
    s1 = pts // k

    if s1 % 2 == 0:
        print("Chef")
    else:
        print("Paja")
