t = int(input())
for T in range(t):
    n = int(input())
    a = list(input())
    c = 0
    if n == 1:
        if a[0] == '0':
            c += 1
        print(c)
    else:
        for i in range(n - 1):
            if i == 0:
                if a[i] == '0' and a[i + 1] == '0':
                  c += 1
            elif i == n - 1:
                if a[i] == '0' and a[i - 1] == '0':
                    c += 1
            else:
                if a[i] == '0' and a[i - 1] == '0' and a[i + 1] == '0':
                    c += 1
            i += 1
    
        if a[n - 1] == "0" and a[n - 2] == '0':
            c += 1
        print(c)
