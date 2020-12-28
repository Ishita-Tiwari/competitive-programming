t = int(input())
for T in range(t):
    a, b = [int(x) for x in input().split()]
    val = str(a + b)
    ans = 0
    for i in val:
        if i == "0" or i == "9" or i == "6": ans += 6
        elif i == "1": ans += 2
        elif i == "7": ans += 3
        elif i == "4": ans += 4
        elif i == "8": ans += 7
        else: ans += 5
    print(ans)
