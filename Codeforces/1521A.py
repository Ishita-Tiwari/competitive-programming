t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]
    good = a * b
    nearly1 = a
    if b == 1:
        print("NO")
        continue
    nearly2 = good + nearly1
    print("YES")
    print(good,nearly1, nearly2)
