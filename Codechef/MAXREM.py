n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if n == 1:
    print("0")
else:
    ind = a.index(a[n - 1])
    if ind == 0:
        print("0")
    else:
        print(a[ind - 1] % a[n - 1])
