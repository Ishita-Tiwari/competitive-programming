pwr = []
for i in range(1, 21):
    pwr.append(pow(2, i))

pwr = set(pwr)

t = int(input())
for T in range(t):
    n = int(input())
    ans = [2, 3, 1]
    if n in pwr:
        print(-1)
        continue

    if n == 1:
        print(1)
        
    else:
        for i in range(4, n + 1):
            ans.append(i)

        for i in range(4, n + 1):
            if i in pwr:
                ans[i - 1], ans[i] = ans[i], ans[i - 1]
        ans = [str(i) for i in ans]
        ans = ' '.join(ans)
        
        print(ans)
