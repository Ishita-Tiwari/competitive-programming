t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    val, k = 0, n
    d = {}
    
    for i in range(n):
        if s[i] in d:
            val = i - d[s[i]]
            if val < k:
                k = val
        d[s[i]] = i
    print(n - k)
