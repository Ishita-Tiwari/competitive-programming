t =  int(input())
for T in range(t):
    l, r = [int(x) for x in input().split()]
    count = 0
    for i in range(l, r + 1):
        val = i % 10
        if val == 2 or val== 3 or val == 9:
            count += 1
    print(count)
