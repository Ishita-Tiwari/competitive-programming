def calc(l, n):
    ans, val = 0, 1
    for i in range(n):
        val = l[i]
        if val % 2 == 1 or val % 4 == 0:
            ans += 1
        for j in range(i + 1, n):
            val *= l[j]
            if val % 2 == 1 or val % 4 == 0:
                ans += 1
    print(ans)

t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    calc(l, n)

