t = int(input())
for T in range(t):
    n = int(input())
    ans = 0
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    for N in range(n):
        ind, val = [int(x) for x in input().split()]
        d[ind] = max(d[ind], val)
    for i in range(1, 9):
        ans += d[i]
    print(ans)
