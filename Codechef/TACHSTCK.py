n, d = [int(x) for x in input().split()]
l = []
for i in range(n):
    l.append(int(input()))
count, i = 0, 1

l.sort()
while(i < n):
    if l[i] - l[i - 1] <= d:
        count += 1
        i += 1
    i += 1
print(count)
