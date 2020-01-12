n = int(input())
num = 2
num1 = num + n
while(True):
    c1, c2 = 0, 0
    num1 = num + n
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            c1 = 1
            break
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            c2 = 1
            break
##    print(num, c1, num1, c2)
    if c1 == 1 and c2 == 1:
        break
    num += 1
print(num1, num)
