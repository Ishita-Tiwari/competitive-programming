n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
mx = max(a)
ind = a.index(mx)
b, ans = [], []
 
if ind != 0:
    c = max(a[0], a[1])
    ans.append([a[0], a[1]])
    b.append(min(a[0], a[1]))
 
    for i in range(2, ind + 1):
        ans.append([c, a[i]])
        b.append(min(c, a[i]))
        c = max(c, a[i])
 
num = len(ans)
c1 = a[ind + 1:] + b
for i in range(q):
    m = int(input())
    if m <= num:
        print(*ans[m - 1])
    else:
        print(mx, c1[(m - num - 1) % (n - 1)])
