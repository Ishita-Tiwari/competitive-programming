n = int(input())
a = [int(x) for x in input().split()]
Q = int(input())
pre = [0, a[0]]
arr = a[:]
arr.sort()
pre2 = [0, arr[0]]
for i in range(1, n):
    pre.append(pre[-1] + a[i])
    pre2.append(pre2[-1] + arr[i])


for q in range(Q):
    tp, l, r = [int(x) for x in input().split()]
    if tp == 1:
        print(pre[r] - pre[l - 1])
    else:
        print(pre2[r] - pre2[l - 1])
