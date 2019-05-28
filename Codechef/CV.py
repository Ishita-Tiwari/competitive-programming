t = int(input())
while(t > 0):
    n = int(input())
    s = input()
    count = 0
    l = list(s)
    vow = "aeiou"
    for i in range(0, n - 1):
        if l[i] not in vow and l[i + 1] in vow:
            count += 1
    print(count)
    t-=1
