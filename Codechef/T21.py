t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]
    a %= 3
    b %= 3
    print((a * b) % 3)
