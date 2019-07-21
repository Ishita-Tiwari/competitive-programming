from math import ceil
n = int(input())
ans = ceil(n // 2)
if n % 2 == 1:
    ans = -ans - 1
print(ans)
