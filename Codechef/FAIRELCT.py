t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a.sort()
    b.sort(reverse = True)
    sm_a = sum(a)
    sm_b = sum(b)
    ans, flag = 0, -1
    
    if sm_a > sm_b:
        print(0)
        continue


    for i in range(min(n, m)):
        if sm_a > sm_b:
            flag = 1
            break
        if a[i] < b[i]:
            sm_a -= a[i]
            sm_b -= b[i]
            sm_a += b[i]
            sm_b += a[i]
            ans += 1
    if sm_a > sm_b:
        flag = 1
    if flag == -1:
        print(flag)
    else:
        print(ans)
