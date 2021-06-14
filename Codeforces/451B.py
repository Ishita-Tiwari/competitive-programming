n = int(input())
l = [int(x) for x in input().split()]
req = l[:]
req.sort()
diff = [0]
for i in range(1, n):
    if l[i] == l[i - 1]:
        diff.append(0)
    elif l[i] > l[i - 1]:
        diff.append(1)
    else:
        diff.append(-1)

start, end = -1, -1
ans = 'yes'

d = [diff[0]]
for i in range(1, n):
    if diff[i] != d[-1]:
        d.append(diff[i])
if d.count(-1) > 1:
    print('no')
elif l == req:
    print('yes')
    print('1 1')
else:
    for i in range(n):
        if diff[i] == -1:
            start = i - 1
            break
    for i in range(n - 1, -1, -1):
        if diff[i] == -1:
            end = i
            break
        
    middle = l[start: end + 1]
    beginning = l[:start]
    ending = l[end + 1:]
    middle.sort()
    result = beginning + middle + ending
    if result == req:
        print('yes')
        print(start + 1, end + 1)
    else:
        print('no')
