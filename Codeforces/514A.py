n = int(input())
ans = ""

if n < 10:
    print(n)
    
else:
    
    while(n > 0):
        dig = n % 10
        if (dig > 4 and dig != 9) or (dig == 9 and n > 9):
            dig = 9 - dig
        ans = ans + str(dig)
        n //= 10
    ans = str(ans)
    ans = ans[::-1]
    print(ans)
