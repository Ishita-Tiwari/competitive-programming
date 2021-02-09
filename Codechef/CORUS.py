t = int(input())
for T in range(t):
    n, q = [int(x) for x in input().split()]
    s = input()
    alp = [0] * 26

    for i in range(n):
        alp[ord(s[i]) - 97] += 1
        
    alp.sort(reverse = True)
    
    for Q in range(q):
        c = int(input())
        if c >= alp[0]:
            print(0)
            continue
        ans = 0
        ind = 0

        while(alp[ind] > c and ind < 25):
            ans += alp[ind] - c
            ind += 1
        ans += max(0, alp[-1] - c)
        print(ans)
