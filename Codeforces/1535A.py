t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    l1 = [max(l[0], l[1]), max(l[2], l[3])]

    l.sort(reverse = True)
    l1.sort(reverse = True)

    if l[0] == l1[0] and l[1] == l1[1]:
        print("YES")
    else:
        print("NO")
