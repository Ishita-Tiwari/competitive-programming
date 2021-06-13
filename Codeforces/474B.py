def binSearch(arr, ele):
    lb, ub = 0, len(arr) - 1
    ind = 0
    while(lb <= ub):
        mid = (lb + ub) // 2
        if arr[mid] == ele:
            ind = (mid + 1)
            break
        if arr[mid] < ele:
            lb = mid + 1
        else:
            if mid > 0:
                if arr[mid - 1] > ele:
                    ub = mid - 1
                else:
                    ind = (mid + 1)
                    break
            else:
                ind = (mid + 1)
                break
    for i in range(max(0, ind - 3), ind + 1):
        if arr[i] >= ele:
            ind = i + 1
            break
    return ind
        

n = int(input())
a = [int(x) for x in input().split()]
pre = [a[0]]
for i in range(1, n):
    pre.append(pre[-1] + a[i])

Q = int(input())
q = [int(x) for x in input().split()]
for val in q:
    print(binSearch(pre, val))
