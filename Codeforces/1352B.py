t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    if (n % 2 and k % 2 == 0) or (n < k):
        print('NO')
        continue
    even = 2 * k
    extra = n - even
    ans = [2] * (k - 1)
    if extra == 0:
        ans.append(2)
        print('YES')
        print(*ans)
        continue
    elif extra > 0 and extra % 2 == 0:
        ans.append(2 + extra)
        print('YES')
        print(*ans)
        continue
    extra = n - k
    ans = [1] * (k - 1)
    if extra == 0:
        ans.append(1)
        print('YES')
        print(*ans)
        continue
    elif extra % 2 == 0:
        ans.append(1 + extra)
        print('YES')
        print(*ans)
        continue
    print('NO')
    
