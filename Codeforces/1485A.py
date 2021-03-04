t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]
    ans = 0
    dup = a
    dup_b = b

    if b == 1:
        b += 1
        ans += 1

    while(a > 0):
        ans += 1
        a //= b
    
    for i in range(1, 100):
        val = 0
        a = dup
        b = dup_b + i
        if b == 1:
            b += 1
            val += 1

        while(a > 0):
            val += 1
            a //= b
##        print(val + i)
        ans = min(ans, i + val)
        

    print(ans)
