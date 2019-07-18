n, m = [int(x) for x in input().split()]
if m == 0 or m == 1:
    print("1")
else:
    ans = min(n - m, m)
    print(ans)
