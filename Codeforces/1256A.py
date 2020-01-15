t = int(input())
for T in range(t):
    a, b, n, s = [int(x) for x in input().split()]

    num = min(a, s // n)
    s -= num * n

    if s <= b:
        print("YES")
    else:
        print("NO")
        
