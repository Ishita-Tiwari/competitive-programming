t = int(input())
for T in range(t):
    n, k, v = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    A = sum(a)
    ans = (v * (n + k)) - A
    ans = ans / k

    if ans == int(ans) and ans > 0:
        print(int(ans))
    else:
        print("-1")
