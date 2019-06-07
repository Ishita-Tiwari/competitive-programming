t = int(input())
for T in range(t):
    n = int(input())
    l = ["0"] * n
    s = ''
    for i in range(n):
        l[i] = input()
        s += l[i]
    c = s.count("c") // 2
    d = s.count("d")
    e = s.count("e") // 2
    f = s.count("f")
    h = s.count("h")
    o = s.count("o")
    num = min(c, e, d, f, h, o)
    print(num)
