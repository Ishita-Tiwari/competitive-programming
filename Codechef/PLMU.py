t = int(input())
for T in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    zero, two = [0] * 2

    for i in range(n):
        if l[i] == 0:
            zero += 1
        elif l[i] == 2:
            two += 1

    ans = (two * (two - 1)) // 2 + (zero * (zero - 1)) // 2
    print(ans)
