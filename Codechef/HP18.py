t = int(input())
for T in range(t):
    n, a, b = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]

    na, nb, nab = 0, 0, 0

    for i in l:
        if i % a == 0:
            na += 1
        elif i % b == 0:
            nb += 1
        elif i % a == 0 and i % b == 0:
            nab += 1
    na -= nab
    nb -= nab

    if na <= nb:
        print("ALICE")
    else:
        print("BOB")
