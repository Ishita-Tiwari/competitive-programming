t = int(input())
for T in range(t):
    n, k, p = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    val, ans = 0, 0
    
    if p == 0 and k % 2 == 1:
        print(max(a))
        continue
    elif p == 0:
        ans = 0

        for i in range(1, n - 1):
            ans = max(ans, min(a[i - 1], a[i + 1]))
            
        print(max(ans, a[1], a[-2]))
        
    elif p == 1 and k % 2 == 1:
        print(min(a))
        continue

    elif p == 1:
        ans = 10 ** 10

        for i in range(1, n - 1):
            ans = min(ans, max(a[i - 1], a[i + 1]))

        print(min(ans, a[1], a[-2]))

    
