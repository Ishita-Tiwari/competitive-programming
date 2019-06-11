t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(sum(l) - (n * min(l)))
