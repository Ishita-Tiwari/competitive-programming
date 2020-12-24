t = int(input())
for T in range(t):
    l = list(input())

    ind = len(l)
    ans = 0
    while(ind > 3):
        val = l[ind - 4: ind]
        
        if val.count('?') == 0:
            ind -= 1
            continue
        
        s1 = ''.join(val)
        if s1 == 'CHEF':
            ind -= 4
            continue

        flag = 0
        if val.count('?') > 0:
            if val[0] != '?' and val[0] != 'C':
                flag = -1
            if val[0 + 1] != '?' and val[0 + 1] != 'H':
                flag = -1
            if val[0 + 2] != '?' and val[0 + 2] != 'E':
                flag = -1
            if val[0 + 3] != '?' and val[0 + 3] != 'F':
                flag = -1

        if flag == 0:
            l[ind - 4] = 'C'
            l[ind - 3] = 'H'
            l[ind - 2] = 'E'
            l[ind - 1] = 'F'
            ind -= 4
            continue

        
        ind -= 1
        
    n_string = ''.join(l)
    n_string = n_string.replace('?', 'A')
    print(n_string)
