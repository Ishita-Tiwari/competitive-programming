t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    one = []
    zero = []

    for i in range(n):
        if b[i]:
            one.append(a[i])
        else:
            zero.append(a[i])

    ans = 'YES'
    if (len(zero) == 0 and one != sorted(one)) or (len(one) == 0 and zero != sorted(zero)):
        ans = 'NO'

    print(ans)
