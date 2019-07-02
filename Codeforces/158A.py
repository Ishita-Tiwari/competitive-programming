n, k = [int(x) for x in input().split()]
l = ['0'] * n
k -= 1
c = 0
l = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    if l[i] >= l[k] and l[i] != 0:
        c += 1
print(c)
