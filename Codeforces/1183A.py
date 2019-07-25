n = int(input())
s = 0
ans = 0
num = 0
for i in range(n, 100000):
    num = i
    while(num > 0):
        s += num % 10
        num //= 10
    if s % 4 == 0:
        ans = i
        break
    else:
        s = 0
print(ans)
