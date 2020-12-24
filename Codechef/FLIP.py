t = int(input())
for T in range(t):
    a = list(input())
    b = list(input())
    n = len(a)

    if a == b:
        print(0)
        continue

    a_odd, b_odd = [], []
    a_even, b_even = [], []
    for i in range(n):
        if i % 2:
            a_odd.append(a[i])
            b_odd.append(b[i])
        else:
            a_even.append(a[i])
            b_even.append(b[i])

    c0, c1 = [], []

    sm = 1
    for i in range(len(a_odd)):
        if a_odd[i] == b_odd[i]:
            c1.append(0)
        else:
            c1.append(1)
    for i in range(len(a_even)):
        if a_even[i] == b_even[i]:
            c0.append(0)
        else:
            c0.append(1)

    v1, v0 = [], []
    v1.append(c1[0])
    v0.append(c0[0])
    for i in range(1, len(c0)):
        if c0[i] != v0[-1]:
            v0.append(c0[i])

    for i in range(1, len(c1)):
        if c1[i] != v1[-1]:
            v1.append(c1[i])

    in_odd = v1.count(1)
    in_even = v0.count(1)

    print(in_odd + in_even)
