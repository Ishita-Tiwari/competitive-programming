t = int(input())
for T in range(t):
    l = int(input())
    d = list(input())
    c1 = 0
    flag = 0
    c = d.count("P")
    curr = (c / l) * 100
    if curr >= 75:
        print("0")
    else:
        for i in range(2, l - 2):
            if d[i] != 'P':
                if ((d[i - 1] == 'P' or d[i - 2] == 'P') and (d[i + 1] == 'P' or d[i + 2] == 'P')):
                    c += 1
                    c1 += 1
            curr = (c / l) * 100
            if curr >= 75:
                flag = 1
                break
            
        if flag == 0:
            print("-1")
        else:
            print(c1)
