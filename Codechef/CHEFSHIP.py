t = int(input())
for T in range(t):
    s = input()
    n = len(s)

    s1 = ""
    count = 0
    for i in range(1, n):
        
        s1 = s[:i]
        s2 = s[i: i * 2]
        l2 = (n - 2 * i) // 2

        s3 = s[i * 2: i * 2 + l2]
        s4 = s[i * 2 + l2:]

        if s1 == s2 and s3 == s4 and s3 != "":
            count += 1
##        print(s1, s2, s3, s4, count)

    print(count)
