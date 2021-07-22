t = int(input())
for T in range(t):
    s = input()
    l = list(s)
    l.sort()
    ans = "YES"
    for i in range(0, len(l)):
        if l[i] != chr(i + 97):
            ans = "NO"
            break

    if ans == "NO":
        print(ans)
        continue
    
    ini = "a"
    prev = s.index('a')
    for i in range(1, len(s)):
        curr_ind = s.index(chr(i + 97))
        prev_ind = s.index(chr(i + 96))

        if curr_ind < prev_ind:
            ini = chr(i + 97) + ini
        else:
            ini = ini + chr(i + 97)

    if ini == s:
        print("YES")
    else:
        print("NO")
