n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
d, s, temp, arr = {}, 0, [], []
arr.append([])

for i in a:
    d[i] = 0
for i in a:
    d[i] += 1

for i in d:
    arr[0].append(d[i])
    s += d[i]
    temp.append(s)

for i in range(1, k):
    arr.append([])
    val = 0
    for j in range(len(arr[0]) - i):
        v = arr[0][j] * (temp[-i] - temp[j])
        arr[i].append(v)
        s += v
        val += v
        temp[j] = val
print((s + 1) % 1000000007)
