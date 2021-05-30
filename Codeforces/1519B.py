t = int(input())
for T in range(t):
    n, m, k = [int(x) for x in input().split()]

    value = n * m - 1
    if value == k:
        print("YES")
    else:
        print("NO")

    
