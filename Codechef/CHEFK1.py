from math import ceil

for _ in range(int(input())):

    n, m = [int(x) for x in input().split()]
    result = 0

    if n == 1:
        if m == 0: result = 0
        elif m == 1: result = 1
        else: result = -1
        
    elif n == 2:
        if m == 1: result = 1
        elif m > 1 and m <= 3: result = 2
        else: result = -1
        
    elif m < n-1 or m > (n*(n+1)//2):
        result = -1
        
    elif m >= n-1 and m <= n+1: result = 2
    
    elif m > n+1 and m <= 2*n: result = 3
        
    else:
        x = m - 2*n
        y = n / 2
        result = ceil(x / y) + 3

    print(result)
