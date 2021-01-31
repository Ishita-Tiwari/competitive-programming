t = int(input())
for T in range(t):
    x, k = [int(x) for x in input().split()]
    val = 0
    
    for i in range(2, int(x ** 0.5) + 1):
        while(x % i == 0):
            x //= i
            val += 1
    if x > 1:
        val += 1
    if val >= k:
        print(1)
    else:
        print(0)
