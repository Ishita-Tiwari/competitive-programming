t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    if (n // k) % k == 0:
        print("NO")
    else:
        print("YES")
