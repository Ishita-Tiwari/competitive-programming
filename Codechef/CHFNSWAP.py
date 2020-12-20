t = int(input())
for T in range(t):
    n = int(input())
    total = (n * (n + 1)) // 2
    
    if n == 3:
        print(2)
        continue
    if total % 2:
        print(0)
        continue
    
    half = total // 2
    ind = 0
    ub, lb = n, 1
    flag = 0
    while(ub >= lb):
        mid = (ub + lb) // 2
        val = (mid * (mid + 1)) // 2
        if half > val:
            lb = mid + 1
        elif half == val:
            ind = mid
            flag = 1
            break
        else:
            if mid > 0:
                if val - mid < half:
                    ind = mid
                    break
            ub = mid - 1
    mx_chng = n - ind + 1
    if flag == 1:
        v1 = n - ind - 1
        mx_chng = (ind * (ind - 1)) // 2 + (v1 * (v1 + 1) // 2)
        
        v2 = 0
##        print(mx_chng)
        
        n -= 1
        total = n * (n + 1) // 2

        if total % 2:
            total -= n
            n -= 1

        if total % 2:
            total -= n
            n -= 1
            
        
        half = total // 2
        ind = 0
        ub, lb = n, 1
        flag = 0
        while(ub >= lb):
            mid = (ub + lb) // 2
            val = (mid * (mid + 1)) // 2
##            print(mid, val, half, end=" ")
            if half > val:
##                print("case 1")
                lb = mid + 1
            elif half == val:
##                print("case 2")
                ind = mid
                flag = 1
                break
            else:
##                print("case 3")
                if mid > 0:
                    if val - mid < half:
                        ind = mid
                        break
                ub = mid - 1
            
        mx_chng += (n - ind + 1)
##        print(n - ind + 1)
        
    print(mx_chng)
