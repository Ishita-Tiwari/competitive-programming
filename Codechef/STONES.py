t = int(input())
for T in range(t):
    j = input()
    s = input()
    c = 0
    for i in s:
        if i in j:
            c += 1
    print(c)
