t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    ans = s
    val, val1 = '', ''
    for i in range(n):
        ##print(val, end = " ")
        val = s[:i] + s[i + 1:]
        for j in range(n):
            val1 = val[:j] + s[i] + val[j:]
            ##print(val1)
            ans = min(ans, val1)
    print(ans)
