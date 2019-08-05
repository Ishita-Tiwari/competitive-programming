t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    r = input()
    if s.count('1') != r.count('1') or s.count('0') != r.count('0'):
        print('NO')
    else:
        print('YES')
