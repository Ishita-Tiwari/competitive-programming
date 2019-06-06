t = int(input())
for T in range(t):
    n = int(input())
    i1, i2 = 0, 0
    s1, s2 = '', ''
    l2 = [0] * n
    l = ['0'] * n
    for i in range(n):
        l[i] = input()
    for i in range(n):
        i1 = l[i].index(" ")
        s1 = l[i][:i1]
        for j in range(i+1, n):
            i2 = l[j].index(" ")
            s2 = l[j][:i2]
            if s1 == s2:
                l2[i] += 1
                l2[j] += 1
            s2 = ''
        s1 = ''
    for i in range(n):
        if l2[i] == 0:
            i1 = l[i].index(" ")
            print(l[i][:i1])
        else:
            print(l[i])
