for T in range(int(input())):
    a = int(input())
    n = 360 / (180 - a)
    if n == int(n):
        print("YES")
    else:
        print("NO")
