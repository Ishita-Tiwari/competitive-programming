
 t = int(input())
for T in range(t):
    k, n, a, b = [int(x) for x in input().split()]
    n1 = n
    jp, p = 0, 0
    c = 0
    if k <= n * b:
        print("-1")
    else:
        if k > n * a:
            print(n)
        else:
            lb = -1
            ub = n + 1
            mid = 0
            while(ub > lb + 1):
                mid = (lb + ub) // 2
                if mid * a + (n - mid) * b < k:
                    lb = mid
                else:
                    ub = mid
            print(lb)
