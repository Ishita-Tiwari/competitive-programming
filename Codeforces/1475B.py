t = int(input())
for T in range(t):
    n = int(input())
    ans = "NO"

    one = n % 2020
    zero = (n - one) // 2020 - one

    if zero >= 0 and 2020 * zero + 2021 * one == n:
        ans = "YES"
    
    print(ans)
