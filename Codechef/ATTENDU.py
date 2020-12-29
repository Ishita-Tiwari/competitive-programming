t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    zero = s.count('0')
    if zero > 30:
        print("NO")
    else:
        print("YES")
