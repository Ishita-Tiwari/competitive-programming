for T in range(int(input())):
    a1, a2, a3, c1, c2, c3 = [int(x) for x in input().split()]
    c = 0
    val = []
    val.append([a1, c1])
    val.append([a2, c2])
    val.append([a3, c3])
    val.sort()
    for i in range(2):
        if val[i][0] == val[i + 1][0]:
            if val[i][1] != val[i + 1][1]:
                c = 1
                break
        else:
            if val[i][1] >= val[i + 1][1]:
                c = 1
                break
    if c == 1:
        print("NOT FAIR")
    else:
        print("FAIR")
