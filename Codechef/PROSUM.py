t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    zero = l.count(0)
    one = l.count(1)
    two = l.count(2)
    val = n - (zero + one + two)
    
    total = two * val + (val * (val - 1)) // 2
    print(total)
