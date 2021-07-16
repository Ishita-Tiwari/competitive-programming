def prod(arr):
    r = 1
    for i in arr:
        r *= i
    return r

t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    neg, pos = 0, 0
    a.sort(reverse = True)
    ans = 1
    res = []
    for i in range(6):
        v = a[:i] + a[n + i - 5:]
        res.append(v)
    for i in range(len(res)):
        if i == 0:
            ans = prod(res[i])
        ans = max(ans, prod(res[i]))
    print(ans)
