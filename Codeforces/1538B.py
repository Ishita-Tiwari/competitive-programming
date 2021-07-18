t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    if sum(a) % n:
        print("-1")
        continue
    a.sort()
    val = sum(a) // n

    if a[0] == a[-1]:
        print(0)
        continue
    
    count = 0
    for i in range(n - 1, -1, -1):
        if a[i] > val:
            count += 1
        else:
            break

    print(count)
