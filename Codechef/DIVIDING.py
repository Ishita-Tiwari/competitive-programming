n = int(input())
l = [int(x) for x in input().split()]
total = sum(l)

if total == (n * (n + 1)) // 2:
    print("YES")
else:
    print("NO")
