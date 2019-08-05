t = int(input())
for T in range(t):
    n = int(input())
    k = int(input())

    rem = k - ((k // n) * n)

    if rem == n - rem:
        print(2 * rem - 1)
    else:
        print(2 * min(rem, n - rem))
