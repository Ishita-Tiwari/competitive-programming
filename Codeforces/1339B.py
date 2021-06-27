t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    a.sort()
    ans = [0] * n

    mid = n // 2 - 1
    if n % 2 == 1:
        mid += 1
    ind = 0
    inc = 1
    change = 0
    while(ind < n):
        if mid < 0 or mid > n - 1:
            break
        ans[ind] = a[mid]
        ind += 1
        change += 1
        if inc:
            mid += change
            inc = 0
        else:
            mid -= change
            inc = 1
            
    print(*ans)
