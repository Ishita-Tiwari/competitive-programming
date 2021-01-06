t = int(input())
for T in range(t):
    n = int(input())
    val = n // 4
    a = [int(x) for x in input().split()]
    x, y, z = 0, 0, 0
    l1, l2, l3, l4 = [], [], [], []
    a.sort(reverse = True)
    ans = 0
    count = 0
    for i in range(n):
        if count < n // 4:
            l1.append(a[i])
        elif count < 2 * (n // 4):
            l2.append(a[i])
        elif count < 3 * (n // 4):
            l3.append(a[i])
        else:
            l4.append(a[i])
        count += 1
    if len(l1) != n / 4 or len(l2) != n // 4 or len(l3) != n // 4 or len(l4) != n // 4:
        ans = -1
    if len(l1) > 0 and len(l2) > 0:
        if l1[-1] == l2[0]:
            ans = -1
    if len(l2) > 0 and len(l3) > 0:
        if l2[-1] == l3[0]:
            ans = -1
    if len(l3) > 0 and len(l4) > 0:
        if l3[-1] == l4[0]:
            ans = -1
    if ans == -1:
        print(ans)
    else:
        ans = l1[-1] + l2[-1] + l3[-1] + l4[-1]
        print(l3[-1], l2[-1], l1[-1])
