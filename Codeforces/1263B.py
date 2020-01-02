t = int(input())
for T in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    count = 0
    num = 0
    for i in range(n):
        l1 = l[:i] + l[i + 1:]
        if l[i] in l1:
            l[i] //= 10
            l[i] *= 10
            for j in range(10):
                if l[i] + j not in l1:
                    l[i] += j
                    count += 1
                    break
                
    
    print(count)
    for i in range(n):
        if len(str(l[i])) < 4:
            l[i] = "0" * (4 - len(str(l[i]))) + str(l[i])
        print(l[i])
    
