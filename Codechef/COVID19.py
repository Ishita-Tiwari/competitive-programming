t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    val = [1] * n

    for i in range(n):
        c = 0
        if i > 0:
            if abs(a[i] - a[i - 1]) <= 2:
                c += 1
                for j in range(i - 1, 0, -1):
                    if abs(a[j] - a[j - 1]) <= 2:
                        c += 1
                    else:
                        break
        if i < n - 1:
            if abs(a[i] - a[i + 1]) <= 2:
                c += 1

                for j in range(i + 1, n - 1):
                    if abs(a[j] - a[j + 1]) <= 2:
                        c += 1
                    else:
                        break

        val[i] += c
    
##    print(val)
    val.sort()
    print(val[0], val[-1])
