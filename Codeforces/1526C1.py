n = int(input())
l = [int(x) for x in input().split()]
l1 = []

for i in range(n):
    l1.append(l[i])
    if sum(l1) >= 0:
        continue
    l1.sort()
    del l1[0]

print(len(l1))
