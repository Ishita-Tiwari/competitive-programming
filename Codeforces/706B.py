n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
a.sort()
 
for Q in range(q):
    val = int(input())
    lb, ub = 0, n - 1
    ans = 0
    
    while(lb <= ub):
        mid = (lb + ub) // 2
 
        if a[mid] <= val:
            lb = mid + 1
            ans = mid + 1
        else:
            ub = mid - 1
    print(ans)
