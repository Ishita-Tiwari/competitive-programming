t = int(input())
for T in range(t):
    n = int(input())
    s = input()
    x, y = 0, 0
    c = ''
    
    for i in s:
        if i == 'R' and c != 'x':
            x += 1
            c = 'x'
        elif i == 'L' and c != 'x':
            x -= 1
            c = 'x'
        elif i == 'U' and c != 'y':
            y += 1
            c = 'y'
        elif i == 'D' and c != 'y':
            y -= 1
            c = 'y'
            

    print(x, y)
