t = int(input())
for T in range(t):
    n = int(input())
    l = []
    for N in range(n):
        l.append([x for x in input().split()])
    l1 = []
    for i in range(1, n):
        l1.append(l[i][0])

    for i in range(n - 1):
        if l1[i] == "Right":
            l1[i] = "Left"
        elif l1[i] == "Left":
            l1[i] = "Right"
    l1.append("Begin")
    l1.reverse()
    l.reverse()

    for i in range(n):
        l[i][0] = l1[i]

    for i in range(n):
        print(*l[i])
