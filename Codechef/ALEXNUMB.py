t = int(input())
for T in range(t):
    n = int(input()) - 1
    l = [int(x) for x in input().split()]
    print((n * (n + 1)) // 2)
