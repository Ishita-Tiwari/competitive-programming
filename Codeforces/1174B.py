n = int(input())
l = [int(x) for x in input().split()]
even, odd = 0, 0
for i in range(n):
    if l[i] % 2 == 0:
        even += 1
    else:
        odd += 1
if even == 0 or odd == 0:
    print(*l)
else:
    l.sort()
    print(*l)
