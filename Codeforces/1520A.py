t = int(input())
for T in range(t):
    n = int(input())
    s = input()

    l = [0] * 26
    ans = "YES"
    for i in range(n):
        ind = ord(s[i]) - 65
        l[ind] += 1
        if l[ind] > 1:
            if s[i - 1] != s[i]:
                ans = "NO"

    

    print(ans)
