t = int(input())
for T in range(t):
    a, b = [x for x in input().split()]
    a = a[::-1]
    b = b[::-1]
    ans = str(int(a) + int(b))[::-1]
    print(int(ans))
