t = int(input())
for T in range(t):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(list(s))
    ans = 0
    for i in range(10):
        count = 0
        for j in range(n):
            count += int(l[j][i])
        if count % 2 == 1:
            ans += 1
    print(ans)
