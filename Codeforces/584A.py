n, t = [int(x) for x in input().split()]
num = (10 ** n) - 1
num2 = (10 ** (n - 1)) - 1
ans = 0
for i in range(num, num2, -1):
    if i % t == 0:
        ans = i
        break
if ans != 0:
    print(ans)
else:
    print("-1")
