t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if n == 1:
        print("YES")
        if a[0] == -1:
            a[0] = 1
        print(a[0])
        continue
    if k == 2:
        if a[0] == -1:
            for i in range(n):
                if a[i] != -1:
                    break
            
            if a[i] != -1:
                if a[i] == 1:
                    if i % 2 == 1:
                        a[0] = 2
                    else:
                        a[0] = 1
                else:
                    if i % 2 == 0:
                        a[0] = 2
                    else:
                        a[0] = 1
            else:
                a[0] = 1

        for i in range(1, n - 1):
            if a[i] == -1:
                if a[i - 1] == a[i + 1] or a[i + 1] == -1:
                    if a[i - 1] == 1:
                        a[i] = 2
                    else:
                        a[i] = 1
                else:
                    print("NO")
                    break
        else:
            i += 1
            print("YES")
            if a[i] == -1:
                if a[i - 1] == 1:
                    a[i] = 2
                else:
                    a[i] = 1
            print(*a)
    else:
        if a[0] == -1:
            if a[1] == 1:
                a[0] = 2
            else:
                a[0] = 1

        for i in range(1, n - 1):
            if a[i] == -1:
                if a[i - 1] == 1 or a[i + 1] == 1:
                    if a[i - 1] == 2 or a[i + 1] == 2:
                        a[i] = 3
                    else:
                        a[i] = 2
                else:
                    a[i] = 1
        else:
            i += 1
            if a[i] == -1:
                if a[i - 1] == 1:
                    a[i] = 2
                else:
                    a[i] = 1
            print("YES")
            print(*a)
