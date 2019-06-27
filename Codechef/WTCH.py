t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    count = 0
    ans = 0
    l = list(s)
    l.sort()
    if l[0] == l[n - 1] and n % 2 == 1:
        print((n // 2) + 1)
    else:
        for i in range(len(s)):
            if s[i] == '0':
                count += 1
            if s[i] == '1' or i == n - 1:
                s = s[i:]
                break
        ans += (count // 2)
        count = 0


        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1
            if s[i] == '1':
                s = s[0:i + 1]
                break
        ans += (count // 2)
        count = 0

    
        for i in s:
            if i == '0':
                count += 1
            else:
                if count <= 2:
                    count = 0
                    continue
                if count % 2 == 0:
                    count -= 1
                ans += (count // 2)
                count = 0

        print(ans)
