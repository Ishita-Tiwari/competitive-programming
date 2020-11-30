t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0

    for i in range(n - 1):
        if a[i] != a[i + 1]:
            count += 2
            if i >= 1 and a[i] != a[i - 1]:
                count -= 1

    print(count)
