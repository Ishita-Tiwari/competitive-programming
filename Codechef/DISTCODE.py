t = int(input())
for T in range(t):
    s = input()
    st = set()
    n = len(s)

    for i in range(n - 1):
        n_str = s[i: i + 2]
        st.add(n_str)

    print(len(st))
