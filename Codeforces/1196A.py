t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    total = sum(l)
    print(total // 2)
