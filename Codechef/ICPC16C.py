t = int(input())
for T in range(t):
    n = int(input())
    sm = n % 9
    
    if sm == 0:
        sm = 1
    else:
        sm += 1
    print(sm)
