t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    s = input()
    l, r = [0] * n, [0] *  n
    
    for i in range(1, n):
        if s[i - 1] == '1':
            l[i] = l[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if s[i + 1] == '1':
            r[i] = r[i + 1] + 1

    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, l[i] + k + r[i + k - 1])
    print(ans)
