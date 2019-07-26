t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    mn = min(a)
    mx = max(a)
    val = mn + k
    diff = abs(val - mx)
    if diff <= k:
        print(val)
    else:
        print("-1")
