p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
t = int(input())
for T in range(t):
    n = int(input())
    ans = 0
    a = [int(x) for x in input().split()]
    a.sort()
    if a[0] != 1:
        print("-1")
    else:
        for i in range(n):
             if a[i] in p:
                 ans = a[i]
                 break
        if ans != 0:
            print(ans)
        else:
            print("-1")
