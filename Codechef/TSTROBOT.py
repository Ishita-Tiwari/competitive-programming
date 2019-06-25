t = int(input())
for T in range(t):
    n, x = [int(x) for x in input().split()]
    s = input()
    l = [0] * (n + 1)
    l[0] = x
    j = 1
    for i in range(n):
        if s[i] == 'R':
            l[j] = l[j - 1] + 1
        else:
            l[j] = l[j - 1] - 1
        j += 1
    ans = len(set(l))
    print(ans)
