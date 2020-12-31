n1, n2, n3 = [int(x) for x in input().split()]
l1, l2, l3 = [], [], []

for i in range(n1):
    l1.append(int(input()))
for i in range(n2):
    l2.append(int(input()))
for i in range(n3):
    l3.append(int(input()))

s = set(l1 + l2 + l3)
ans = []
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)
count = 0

for i in s:
    count = 0
    if i in s1:
        count += 1
    if i in s2:
        count += 1
    if i in s3:
        count += 1

    if count > 1:
        ans.append(i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
