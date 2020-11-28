t = int(input())
for T in range(t):
    s = input()
    flag = 0
    l = list(s)
    st = set(s)
    if len(st) != 2:
        print("NO")
    else:
        v1, v2 = l[0], l[1]
        if v1 == v2:
            flag = -1
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != l[0]:
                flag = -1
                break
            if i % 2 == 1 and s[i] != l[1]:
                flag = -1
                break
        if flag == -1:
            print("NO")
        else:
            print("YES")
