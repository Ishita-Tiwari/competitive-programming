t = int(input())
for T in range(t):
    a, n = [int(x) for x in input().split()]
    ans = pow(a, n, 9)
    if a != 0 and ans == 0:
        ans = 9
    print(ans)
