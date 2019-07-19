a = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = input()
l = len(n)
c = 0
for i in n:
    if i == '4' or i =='7':
        c += 1
if l == c:
    print("YES")
else:
    c = -1
    num = int(n)
    for i in a:
        if i > num:
            break
        else:
            if num % i == 0:
                c = 0
                break
    if c == 0:
        print("YES")
    else:
        print("NO")
