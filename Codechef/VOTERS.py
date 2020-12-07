n1, n2, n3 = [int(x) for x in input().split()]
d = {}
ans = []

for i in range(n1 + n2 + n3):
    x = int(input())
    if x not in d:
        d[x] = 1
    else:
        ans.append(x)
ans = list(set(ans))
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
