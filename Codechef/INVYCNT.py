t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    rep = 0
    ans = 0
    for i in range(n):
        for j in range(i):
            if a[i] < a[j]:
                rep += 1
    
    if rep == 0 or k == 1:
        print(rep)
        continue

    l = a[:]
    l1 = [0] * n
    for i in range(n):
        count = 0
        for j in range(n):
            if l[j] > l[i]:
                count += 1
        l1[i] = count
    
    
    for i in range(n):
        ans += (k - 1) * l1[i]
    
    ans += k * rep

    
    ans1 = k * rep
    val = sum(l1)
    val *= (k * (k - 1) // 2)
    print(ans1 + val)
