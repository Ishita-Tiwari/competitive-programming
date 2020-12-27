t = int(input())
for T in range(t):
    n = int(input())
    l = [3, 0, 9, 2]
    if n == 1:
        print("0")
    elif n > 1 and n < 4:
        print("1")
    elif n >= 4 and n < 8:
        print("2")
    else:
        ind = 0
        for i in range(63, 2, -1):
            val = pow(2, i)
            #print("Entered the loop")
            if n < val and n >= val // 2:
                #print(val, n, val // 2)
                ind = i
                break
        print(l[ind % 4])
