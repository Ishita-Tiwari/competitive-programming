t = int(input())
for T in range(t):
    s = input()
    n = len(s)
    p = input()
    ele = p[0]
    l = [x for x in s]
    l1 = []

    d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
         'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
         'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
         'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
         'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for i in s:
        d[i] += 1
    for i in p:
        d[i] -= 1

    for i in d:
        if d[i] > 0:
            l1.append(i * d[i])
    l1.sort()

    ans1, ans2 = '', ''
    cnt = 0
    for i in range(len(l1)):
        if (l1[i][0] <= ele):
            ans1 += l1[i]
        else:
            if cnt == 0:
                cnt += 1
                ans1 += p
            ans1 += l1[i]

    cnt = 0
    for i in range(len(l1)):
        if (l1[i][0] < ele):
            ans2 += l1[i]
        else:
            if cnt == 0:
                cnt += 1
                ans2 += p
            ans2 += l1[i]
    if len(ans1) - n != 0:
        ans1 += p
    if len(ans2) - n != 0:
        ans2 += p

    
    ans = [ans1, ans2]
    ans.sort()
    print(ans[0])
