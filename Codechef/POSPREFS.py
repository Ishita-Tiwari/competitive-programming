def check(ans, k):
    pre = []
    pre.append(ans[0])
    for i in range(1, len(ans)):
        pre.append(ans[i] + pre[-1])

    val = 0
    for i in range(len(pre)):
        if pre[i] > 0:
            val += 1
    print(*pre)
    if val == k:
        print("correct ans")
    else:
        print("wrong ans")

t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    dup_k = k

    ans = []

    for i in range(n):
        if k == 0:
            ans.append(-(i + 1))
            continue
        
        if i == 0:
            ans.append(i + 1)
            k -= 1
        elif i == 1:
            ans.append(i + 1)
            k -= 1
        elif i % 2 == 0:
            ans.append(-(i + 1))
        else:
            ans.append(i + 1)
            k -= 1

    for i in range(n - 1, -1, -1):
        if k == 0:
            break
        if ans[i] < 0:
            ans[i] *= -1
            k -= 1
            
##    check(ans, dup_k)
    print(*ans)
##    print("\n\n")
