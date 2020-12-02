t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l1 = []
    l1.append(l[0])
    for i in range(1, n):
        l1.append(min(l1[-1], l[i]))
    print(sum(l1))
