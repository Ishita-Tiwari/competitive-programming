t = int(input())
for _ in range(t):
    n = int(input())
    l = [0] * n
    for i in range(n):
        l[i] = [int(x) for x in input().split()]

    for i in range(n-2, -1, -1):
        for j in range(len(l[i])):
            l[i][j] += max(l[i+1][j], l[i+1][j+1])
    print(l[0][0])
