t = int(input())
for i in range(t):

    a = input()
    b = input()
    st = set(list(a) + list(b))
    ans = 0

    for i in st:
        ans += min(a.count(i), b.count(i))
    print(ans)
