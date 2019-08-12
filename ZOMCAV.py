t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    h.sort()
    ind1 = 0
    ind2 = 0
    
    l = [0] * (n + 1)
    ans = [0] * n
    for i in range(n):
        ind1 = max((i - a[i]), 0)
        ind2 = min((i + a[i]), n - 1)
        l[ind1] += 1
        l[ind2 + 1] -= 1
    ans[0] += l[0]
    for i in range(1, n):
        ans[i] = ans[i - 1] + l[i]
    ans.sort()
    if h == ans:
        print("YES")
    else:
        print("NO")
