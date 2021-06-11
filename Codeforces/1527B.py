t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    c1, c0 = s.count('1'), s.count('0')

    if n % 2:
        if c0 == 1:
            print("BOB")
        else:
            if s[n // 2] == '1':
                print('BOB')
            else:
                print('ALICE')
    else:
        print('BOB')
