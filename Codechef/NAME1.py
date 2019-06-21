for _ in range(int(input())):
    a, b = [x for x in input().split()]
    P = a + b
    flag = 0
    p = [0] * 26
    c = [0] * 26
    n = int(input())
    s = ""
    for i in range(n):
        s += input()
    for i in P:
        p[ord(i) - 97] += 1
    for i in s:
        c[ord(i) - 97] += 1
    for i in range(26):
        if c[i] > 0 and p[i] < c[i]:
            flag = -1
        
    if flag == 0:
        print("YES")
    else:
        print("NO")
