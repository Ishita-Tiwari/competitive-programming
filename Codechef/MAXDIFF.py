t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort()

    #case 1: Lighter k objects
    c1 = sum(l[k:]) - sum(l[:k])

    l.reverse()
    #case 2: Heavier k objects
    c2 = sum(l[k:]) - sum(l[:k])

    print(max(abs(c1), abs(c2)))
