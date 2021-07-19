t = int(input())
for T in range(t):
    n, l, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    
    count, i, ind = 0, 0, 0
    while i < n:
        n -= 1
        while i < n and a[i] + a[n] < l:
            i += 1
        while ind < n and a[ind] + a[n] <= r:
            ind += 1

        count += min(n, ind) - i
        

    print(count)
