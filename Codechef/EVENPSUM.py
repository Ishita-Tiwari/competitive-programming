t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]

    odd_a, odd_b = a // 2, b // 2
    if a % 2:
        odd_a += 1
    if b % 2:
        odd_b += 1
    even_a, even_b = a // 2, b // 2

    ans = odd_a * odd_b + even_a * even_b
    print(ans)
