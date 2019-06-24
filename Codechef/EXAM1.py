t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    u = input()
    ans = 0
    i = 0
    while(i < n):
        if s[i] == u[i]:
            ans += 1
            i += 1
        elif u[i] == 'N':
            i += 1
        
        else:
            i += 2
    print(ans)
