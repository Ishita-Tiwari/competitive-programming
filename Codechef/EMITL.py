t = int(input())
for T in range(t):
    s = input()
    l = s.count("L")
    t = s.count("T")
    i = s.count("I")
    m = s.count("M")
    e = s.count("E")

    if min(l, t, i, m, e) >= 2 and len(s) > 9:
        print("YES")
    elif min(l, t, i, m) >= 2 and e >= 1 and len(s) == 9:
        print("YES")
    else:
        print("NO")
