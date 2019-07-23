n = int(input())
a = [int(x) for x in input().split()]
ans = a.index(max(a))
a = a[::-1]
ans += a.index(min(a))
if ans >= n:
    ans -= 1
print(ans)
