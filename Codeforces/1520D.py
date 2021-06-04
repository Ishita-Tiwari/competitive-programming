t = int(input())
for T in range(t):
    n = int(input())

    a = [int(x) for x in input().split()]
    d = dict()
    
    ## a[j] - a[i] = j - i  =>  a[j] - j = a[i] - i
    for i in range(n):
        val = a[i] - i
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1

    ## getting the number of pairs
    ans = 0
    for i in d:
        ans += (d[i] * (d[i] - 1)) // 2

    print(ans)
