t = int(input())
for T in range(t):
    n = int(input())
    min = 0
    l = [int(x) for x in input().split()]
    l.sort()
    min = l[1] - l[0]
    for i in range(n-1, 0, -1):
        if l[i] - l[i-1]  < min:
            min = l[i] - l[i - 1]
    print(min)
