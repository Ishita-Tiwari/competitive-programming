t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a1 = a[:]
    a1.sort()
    num = 0
    for i in range(n):
        a1[i] = a1[n - 1] - a1[i]
        num += a1[i]
    if num > m:
        print("No")
    else:
        if num == m:
            print("Yes")
        else:
            if (m - num) % n == 0:
                print("Yes")
            else:
                print("No")
