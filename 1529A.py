t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]

    l.sort()
    avg = sum(l) / n

    while(l and avg < l[-1]):
        avg1 = 0
        count = 0
        for i in range(len(l)):
            if i >= len(l):
                break
            if l[i] > avg:
                del l[i]
        avg = sum(l) / len(l)

    print(n - len(l))
