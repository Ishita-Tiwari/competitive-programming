n = int(input())
val, c = 0, 0
for i in range(max(0, n - 97), n + 1):
    val, s1, s2 = i, 0, 0
    n1 = i
    while(n1 > 0):
        s1 += n1 % 10
        n1 //= 10
    val += s1
    while(s1 > 0):
        s2 += s1 % 10
        s1 //= 10
    val += s2
    if val == n:
        c += 1
print(c)
