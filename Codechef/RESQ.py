t = int(input())
for T in range(t):
    n = int(input())
    ans = n - 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ans = min(ans, abs(i - n / i))

    print(int(ans))
