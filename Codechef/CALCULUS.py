def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 

        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x

n = int(input())
ans = 0
m = 998244353

for i in range(1, 2 * n, 2):
    ans = (ans % m + modInverse(i, m) % m) % m

ans *= 2
print(ans % m)
