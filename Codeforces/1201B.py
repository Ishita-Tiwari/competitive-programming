n = int(input())
a = [int(x) for x in input().split()]
a.sort()
s = sum(a)
if a[n - 1] <= s - a[n - 1] and s % 2 == 0:
    print("YES")
else:
    print("NO")
