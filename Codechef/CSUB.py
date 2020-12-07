t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    v = s.count('1')
    print((v * (v + 1)) // 2)
