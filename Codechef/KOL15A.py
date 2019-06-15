t = int(input())
for T in range(t):
    s = input()
    ans = 0
    for i in s:
        if i.isdigit() == True:
            ans += int(i)
    print(ans)
