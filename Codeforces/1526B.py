t = int(input())
for T in range(t):
    n = int(input())
    val = (n % 11) * 111
    ans = 'YES'

    if val > n:
        ans = 'NO'

    print(ans)
