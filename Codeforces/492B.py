n, l = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
diff = []

for i in range(1, len(arr)):
    diff.append(abs(arr[i] - arr[i - 1]) / 2)

if arr[0] != 0:
    diff.append(arr[0])
if arr[-1] != l:
    diff.append(l - arr[-1])

print(max(diff))
