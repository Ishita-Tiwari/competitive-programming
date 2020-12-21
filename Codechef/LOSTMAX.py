t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    ind = l.index(len(l) - 1)
    del l[ind]

    l.sort()
    print(l[-1])
