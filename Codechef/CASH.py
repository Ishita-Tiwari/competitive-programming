t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l = [0] * n
    
    for i in range(n):
        l[i] = a[i] % k
    print(sum(l) % k)
