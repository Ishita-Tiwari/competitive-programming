def logic(a, b, c):
    tot = a + 2 * b + 3 * c
    
    if tot % 2 == 1:
        return "NO"
    if (a, c) == (0, 0):
        if b % 2 == 1:
            return "NO"
        return "YES"
    if (a, b) == (0, 1):
        return "NO"
    if (a, b) == (1, 0):
        return "NO"
    return "YES"

t=int(input())
for x in range(t):
    a, b, c = [int(x) for x in input().split()]
    print(logic(a, b, c))
    
