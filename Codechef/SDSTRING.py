t = int(input())
for T in range(t):
    s = input()
    n = len(s)
    if len(s) % 2 or s.count('1') == n or s.count('0') == n:
        print(-1)
        continue
    print(min(abs(n // 2 - s.count('1')), abs(n // 2 - s.count('0'))))
