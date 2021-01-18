n, q = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l1 = []
vn, vx = 1, 1
count = 0

for i in range(n - 1):
    if l[i] > l[i + 1]:
        l1.append(0)
    elif l[i] < l[i + 1]:
        l1.append(1)
        

for Q in range(q):
    left, right = [(int(x) - 1) for x in input().split()]

    
    if l1[left] != l1[right - 1]:
        print("YES")
    else:
        print("NO")
