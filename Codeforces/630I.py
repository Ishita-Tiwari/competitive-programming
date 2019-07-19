def binexpo(a, b):
    if b == 0:
        return(1)
    res = binexpo(a, b // 2)
    if b % 2 == 1:
        return(res * res * a)
    else:
        return(res * res)
 
n = int(input())
n1 = binexpo(4, n - 2)
n2 = n1 // 4
ans = (6 * n1) + ((n - 3) * 9 * n2)
print(ans)
