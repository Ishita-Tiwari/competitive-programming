t = int(input())
for T in range(t):
    n = int(input())
    l = [0, n]
    st = set(l)

    for i in range(1, int(n ** 0.5) + 1):
        st.add(i)
        st.add(n // i)
        
    print(len(st))
    print(*sorted(st))
