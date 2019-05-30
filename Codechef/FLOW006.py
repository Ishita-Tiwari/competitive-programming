t = int(input())
while(t > 0):
    n = input()
    l = list(n)
    sum = 0
    for i in range(len(n)):
        sum += int(l[i])
    print(sum)
    t -= 1
