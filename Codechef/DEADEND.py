t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    s = set(a)
    count = 0
    
    for i in range(n):
        if a[i] + 1 in s or a[i] - 1 in s:
            continue
        if a[i] + 1 not in s and a[i] - 1 not in s:
            s.add(a[i] + 1)
            count += 1

    print(count)
