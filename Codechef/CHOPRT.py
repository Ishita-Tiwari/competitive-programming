t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
