from math import sqrt

def prime(i):
    num = int(sqrt(i))
    if i % 2 == 0 or num * num == i:
        return False
    else:
        for j in range(3, num + 1, 2):
            if i % j == 0:
                return False
        return True

for T in range(int(input())):
    m, n = [int(x) for x in input().split()]
    
    for i in range (m, n+1):
        if prime(i) or i == 2:
            print(i)
                
    print()
