t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    val = 0
    ind = -1

    for i in range(n):
        if val + a[i] >= k:
            val += (a[i] - k)
        else:
            print("NO", i + 1)
            ind = 0
            break
    if ind == -1:
        print("YES")
