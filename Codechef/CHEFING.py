t = int(input())
for T in range(t):
    n = int(input())
    ans = 0
    l = [0] * 26
    st = set()
    for i in range(n):
        s = input()
        st = set()
        for i in s:
            if i not in st:
                l[ord(i) - 97] += 1
                st.add(i)
        for i in range(26):
            if l[i] == n:
                ans += 1
    print(ans)
