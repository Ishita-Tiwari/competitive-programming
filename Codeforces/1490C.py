st = set()
for i in range(1, 10**4):
    st.add(pow(i, 3))

t = int(input())
for T in range(t):
    n = int(input())

    ans = 'No'

    for i in range(1, n):
        v1 = pow(i, 3)
        if v1 > n:
            break
        v2 = n - v1
        if v2 in st:
            ans = 'Yes'
            break

    print(ans)
