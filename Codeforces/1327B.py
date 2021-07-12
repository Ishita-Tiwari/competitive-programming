t = int(input())
for T in range(t):
    n = int(input())
    l = []
    d = [i + 1 for i in range(n)]
    p = [i + 1 for i in range(n)]
    d, p = set(d), set(p)

    for i in range(n):
        l.append([int(x) for x in input().split()][1:])

    for i in range(n):
        ind = 0
        while(ind < len(l[i])):
            if l[i][ind] in p:
                p.remove(l[i][ind])
                d.remove(i + 1)
                break
            ind += 1

    if len(d) == 0:
        print('OPTIMAL')
    else:
        print('IMPROVE')
        print(d.pop(), p.pop())
