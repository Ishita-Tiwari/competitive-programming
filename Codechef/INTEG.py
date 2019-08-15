n = int(input())
a = [int(x) for x in input().split()]
x = int(input())
l = []
c = 0

for i in range(n):
    if a[i] < 0:
        l.append(-a[i])
l.sort()
ll = len(l)
num = ll - x

ans = 0
for i in range(len(l)):
    l[i] = c - l[i]
    if ll > x:
        ans += abs(l[i] * x)
        c += abs(l[i])
    else:
        ans += abs(l[i] * ll)
        c += abs(l[i])
    ll -= 1
    
print(ans)
