t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 1

    for i in range(len(l)):
        ans *= (l[i] - i)
    print(ans % 1000000007)
