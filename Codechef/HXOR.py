import math

t = int(input())
for T in range(t):
    n, val_x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    
    ind = 0
    nxt = 1
    while(ind < n - 1 and val_x > 0):
        if a[ind] == 0:
            ind += 1
            continue
        
        pow_of_two = pow(2, int(math.log(a[ind], 2)))
        a[ind]^=pow_of_two

        ind2 = ind + 1
        while(True):
            if ind2 == n - 1:
                a[ind2] ^= pow_of_two
                break
            if a[ind2] ^ pow_of_two <= a[ind2]:
                a[ind2] ^= pow_of_two
                break
            ind2 += 1
        val_x -= 1


    if val_x == 1 or (n == 2 and val_x % 2):
        pow_of_two = pow(2, 0)
        a[-1] ^= pow_of_two
        a[-2] ^= pow_of_two
    

    print(*a)
