t = int(input())
for T in range(t):
    n, m, k = [int(x) for x in input().split()]
    c = []
    ans = []
    for N in range(n):
        c.append([int(x) for x in input().split()])
        ans.append(max(c[N]))
        
    print(*ans)
