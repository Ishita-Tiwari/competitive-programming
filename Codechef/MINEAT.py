from math import ceil

def cal(n):
    val = 0
    for i in a:
        val += ceil(i / n)
    return(val)

t = int(input())
for T in range(t):
    n, h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    ans, lb, ub = 0, 1, a[n - 1]

    while(lb <= ub):
        mid = (lb + ub) // 2
        val = cal(mid)
        if val <= h:
            ans = mid
            ub = mid - 1
        else:
            lb = mid + 1
    print(ans)
