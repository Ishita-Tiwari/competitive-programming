t = int(input())
for T in range(t):
    n = int(input())
    ans = "NO"
    
    while(n % 2 == 0):
        n //= 2
    if n % 2 and n != 1:
        ans = "YES"
    print(ans)
