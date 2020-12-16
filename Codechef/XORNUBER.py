t = int(input())
for T in range(t):
    n = int(input())
    b = bin(n)[2:]
    
    if n==1:
        print(2)
    else:
        if '0' in b:
            print(-1)
        else:
            print((n-1)//2)
