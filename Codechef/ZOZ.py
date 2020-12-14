t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]

    total = sum(l)
    count = 0
    for i in range(n):
        if l[i] + k > total - l[i]:
            count += 1

    print(count)
